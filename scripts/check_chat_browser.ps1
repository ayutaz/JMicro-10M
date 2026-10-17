param([int]$Port=7864,[int]$DebugPort=9237,[int]$AttachPID=0,[ValidatePattern('^[a-z0-9_-]+\.json$')][string]$EvidenceName='browser.json')
$ErrorActionPreference='Stop'
$workspace=Split-Path -Parent $PSScriptRoot
$root=Join-Path $workspace 'reports/phase7/chat-response-diagnosis-20261017'
$target=Join-Path $root $EvidenceName
if(Test-Path -LiteralPath $target){throw 'Preserve previous browser evidence'}
$browser='C:/Program Files/Google/Chrome/Application/chrome.exe'
if(!(Test-Path -LiteralPath $browser)){$browser='C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'}
$profile=Join-Path $workspace 'reports/local/chat-browser-diagnosis-profile'
$browserArguments=@('--headless=new','--disable-gpu','--no-first-run','--no-default-browser-check',"--remote-debugging-port=$DebugPort",'--remote-debugging-address=127.0.0.1',('--user-data-dir="'+$profile+'"'),'about:blank')
$worker=if($AttachPID){
    $prior=Get-Content -LiteralPath (Join-Path $root 'browser.json') -Raw|ConvertFrom-Json
    $existing=Get-Process -Id $AttachPID -ErrorAction Stop
    if($prior.helper_pid -ne $AttachPID -or $existing.StartTime.ToUniversalTime().Ticks -ne ([DateTime]$prior.helper_start).ToUniversalTime().Ticks){throw 'Existing browser identity differs'}
    $existing
}else{Start-Process -FilePath $browser -ArgumentList $browserArguments -WindowStyle Hidden -PassThru}
$workerStart=$worker.StartTime.ToUniversalTime().ToString('o')
$socket=[System.Net.WebSockets.ClientWebSocket]::new()
$script:serial=0;$script:events=[System.Collections.Generic.List[object]]::new()
function CDP([string]$method,$parameters){
    $script:serial++;$id=$script:serial
    $bytes=[System.Text.Encoding]::UTF8.GetBytes((@{id=$id;method=$method;params=$parameters}|ConvertTo-Json -Depth 60 -Compress))
    $timeout=[System.Threading.CancellationTokenSource]::new(20000)
    try{
        $null=$socket.SendAsync([System.ArraySegment[byte]]::new($bytes),[System.Net.WebSockets.WebSocketMessageType]::Text,$true,$timeout.Token).GetAwaiter().GetResult()
        while($true){
            $memory=[System.IO.MemoryStream]::new()
            do{
                $buffer=[byte[]]::new(65536)
                $received=$socket.ReceiveAsync([System.ArraySegment[byte]]::new($buffer),$timeout.Token).GetAwaiter().GetResult()
                if($received.MessageType -eq [System.Net.WebSockets.WebSocketMessageType]::Close){throw 'Browser closed connection'}
                $memory.Write($buffer,0,$received.Count)
            }while(!$received.EndOfMessage)
            $message=[System.Text.Encoding]::UTF8.GetString($memory.ToArray())|ConvertFrom-Json -Depth 80
            $memory.Dispose()
            if($message.id -eq $id){if($message.error){throw ($message.error|ConvertTo-Json -Compress)};return $message.result}
            if($message.method){$script:events.Add($message)}
        }
    }finally{$timeout.Dispose()}
}
function JS([string]$expression){
    $r=CDP 'Runtime.evaluate' @{expression=$expression;awaitPromise=$true;returnByValue=$true}
    if($r.exceptionDetails){throw ($r.exceptionDetails|ConvertTo-Json -Depth 10 -Compress)}
    return $r.result.value
}
$report=[ordered]@{observed_at=[DateTime]::UtcNow.ToString('o');url="http://127.0.0.1:$Port";browser=$browser;helper_pid=$worker.Id;helper_start=$workerStart;status='running';conversations=@();mocked_requests=$false}
try{
    $page=$null
    for($attempt=0;$attempt -lt 150;$attempt++){
        try{$pages=Invoke-RestMethod "http://127.0.0.1:$DebugPort/json/list" -TimeoutSec 2;$page=$pages|Where-Object type -eq 'page'|Select-Object -First 1;if($page){break}}catch{}
        Start-Sleep -Milliseconds 200
    }
    if(!$page){throw 'Dedicated browser did not expose a page'}
    $null=$socket.ConnectAsync([Uri]$page.webSocketDebuggerUrl,[System.Threading.CancellationToken]::None).GetAwaiter().GetResult()
    $null=CDP 'Runtime.enable' @{};$null=CDP 'Network.enable' @{};$null=CDP 'Page.enable' @{}
    $null=CDP 'Page.navigate' @{url="http://127.0.0.1:$Port"}
    $report.page=JS '(async()=>{for(let i=0;i<100;i++){if(document.querySelector("#input")&&document.querySelector("#model")?.textContent.includes("M"))return {title:document.title,model:document.querySelector("#model").textContent,footer:document.querySelector("footer").textContent,options:[...document.querySelector("#length").options].map(x=>Number(x.value)),selected:Number(document.querySelector("#length").value)};await new Promise(r=>setTimeout(r,50));}throw Error("Page not ready")})()'
    $cases=@(
        @{name='fresh_greeting';users=@('こんにちは。')},
        @{name='fresh_name_a';users=@('私の名前はあおいです。私の名前だけ答えて。')},
        @{name='fresh_name_b';users=@('私の名前はけんたです。私の名前だけ答えて。')},
        @{name='actual_history';users=@('こんにちは。','今日は疲れています。','少し休むことにしました。','私の名前はあおいです。','さっき伝えた名前を答えて。','名前はけんたに訂正します。今の名前は？')},
        @{name='same_greeting_after_reset';users=@('こんにちは。')}
    )
    foreach($case in $cases){
        $reset=JS '(()=>{document.querySelector("#reset").click();return {messages:document.querySelectorAll(".message").length,input:document.querySelector("#input").value};})()'
        if($reset.messages -ne 0 -or $reset.input -ne ''){throw 'New conversation did not clear the UI'}
        $turns=@()
        foreach($text in $case.users){
            $json=ConvertTo-Json -InputObject $text -Compress
            $expression='(async()=>{const input=document.querySelector("#input");input.value='+$json+';document.querySelector("#form").requestSubmit();for(let i=0;i<300;i++){await new Promise(r=>setTimeout(r,50));if(!document.querySelector("#send").disabled){const rows=[...document.querySelectorAll(".message")].map(n=>({role:n.classList.contains("assistant")?"assistant":"user",text:[...n.childNodes].filter(x=>x.nodeType===Node.TEXT_NODE).map(x=>x.textContent).join("")}));return {messages:rows,status:document.querySelector("#status").textContent,error:document.querySelector("#status").classList.contains("error")};}}throw Error("UI request timeout");})()'
            $row=JS $expression
            if($row.error){throw $row.status}
            $turns+=@{user=$text;UI=$row}
            [PSCustomObject]@{conversation=$case.name;user=$text;reply=$row.messages[-1].text}|ConvertTo-Json -Compress|Write-Output
        }
        $report.conversations+=@{name=$case.name;reset=$reset;turns=$turns}
    }
    $requests=@($script:events|Where-Object {$_.method -eq 'Network.requestWillBeSent' -and $_.params.request.url -eq "http://127.0.0.1:$Port/api/chat"})
    $network=@()
    foreach($request in $requests){$body=CDP 'Network.getResponseBody' @{requestId=$request.params.requestId};$network+=@{request=($request.params.request.postData|ConvertFrom-Json -Depth 60);response=($body.body|ConvertFrom-Json -Depth 60)}}
    $report.network=$network
    if($network.Count -ne 10){throw 'Not all ten actual UI requests captured'}
    for($i=0;$i -lt 6;$i++){$expected=2*$i+1;if($network[3+$i].request.messages.Count -ne $expected){throw 'Actual browser history length differs'}}
    if($network[9].request.messages.Count -ne 1){throw 'Reset retained old request history'}
    $report.actual_history_and_reset_verified=$true
    $shot=CDP 'Page.captureScreenshot' @{format='png';captureBeyondViewport=$true}
    [System.IO.File]::WriteAllBytes((Join-Path $root ([System.IO.Path]::GetFileNameWithoutExtension($EvidenceName)+'.png')),[Convert]::FromBase64String($shot.data))
    $report.status='actual_browser_requests_and_history_complete'
}catch{$report.status='failed_partial_preserved';$report.error=$_.Exception.Message;throw}
finally{
    $report|ConvertTo-Json -Depth 80|Set-Content -LiteralPath $target -Encoding utf8
    if($socket.State -eq [System.Net.WebSockets.WebSocketState]::Open){try{$null=CDP 'Browser.close' @{}}catch{}}
    $socket.Dispose()
}
