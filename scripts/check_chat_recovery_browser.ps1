param([ValidateSet('C0','C1')][string]$Arm='C1',[int]$AttachPID=0)
$ErrorActionPreference='Stop'
$workspace=Split-Path -Parent $PSScriptRoot
$Port=if($Arm -eq 'C1'){7866}else{7867}
$DebugPort=if($Arm -eq 'C1'){9238}else{9239}
$root=Join-Path $workspace "reports/phase7/chat-recovery-20261018/input-structure-main/practical/$Arm"
New-Item -ItemType Directory -Force -Path $root | Out-Null
$target=Join-Path $root 'browser.json'
$model=Invoke-RestMethod "http://127.0.0.1:$Port/api/model" -TimeoutSec 5
if($model.config_sha256 -ne '29a5fa2541f321a8de26f4f54ee98879bfc2245f232ebfe5246d09069d65f075' -or $model.arm -ne $Arm -or $model.device -ne 'CPU' -or $model.max_new_tokens -ne 32){throw 'Actual CPU model differs from the frozen comparison'}
$browser='C:/Program Files/Google/Chrome/Application/chrome.exe'
if(!(Test-Path -LiteralPath $browser)){$browser='C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'}
$profile=Join-Path $workspace "reports/local/chat-input-structure-browser-$Arm"
$arguments=@('--headless=new','--disable-gpu','--no-first-run','--no-default-browser-check',"--remote-debugging-port=$DebugPort",'--remote-debugging-address=127.0.0.1',('--user-data-dir="'+$profile+'"'),'about:blank')
if($AttachPID){
    $prior=Get-Content -LiteralPath $target -Raw | ConvertFrom-Json -Depth 80
    $ownedProcess=Get-Process -Id $AttachPID -ErrorAction Stop
    if($prior.helper_pid -ne $AttachPID -or $ownedProcess.StartTime.ToUniversalTime().Ticks -ne ([DateTime]$prior.helper_start).ToUniversalTime().Ticks -or $prior.conversations.Count -gt 0 -or $prior.in_progress_conversation.turns.Count -gt 0){throw 'Only the same verified helper before any model response may attach'}
    Copy-Item -LiteralPath $target -Destination (Join-Path $root 'browser-initial-observation.json')
}else{
    if(Test-Path -LiteralPath $target){throw 'Prior browser evidence exists; inspect actual helper and partial state before any new start'}
    $ownedProcess=Start-Process -FilePath $browser -ArgumentList $arguments -WindowStyle Hidden -PassThru
}
$socket=[System.Net.WebSockets.ClientWebSocket]::new()
$script:serial=0;$script:events=[System.Collections.Generic.List[object]]::new()
function CDP([string]$method,$parameters){
    $script:serial++;$id=$script:serial
    $bytes=[Text.Encoding]::UTF8.GetBytes((@{id=$id;method=$method;params=$parameters}|ConvertTo-Json -Depth 80 -Compress))
    $timeout=[Threading.CancellationTokenSource]::new(20000)
    try{
        $null=$socket.SendAsync([ArraySegment[byte]]::new($bytes),[System.Net.WebSockets.WebSocketMessageType]::Text,$true,$timeout.Token).GetAwaiter().GetResult()
        while($true){
            $memory=[IO.MemoryStream]::new()
            do{
                $buffer=[byte[]]::new(65536);$received=$socket.ReceiveAsync([ArraySegment[byte]]::new($buffer),$timeout.Token).GetAwaiter().GetResult()
                if($received.MessageType -eq [System.Net.WebSockets.WebSocketMessageType]::Close){throw 'Browser connection closed'}
                $memory.Write($buffer,0,$received.Count)
            }while(!$received.EndOfMessage)
            $message=[Text.Encoding]::UTF8.GetString($memory.ToArray()) | ConvertFrom-Json -Depth 100;$memory.Dispose()
            if($message.id -eq $id){if($message.error){throw ($message.error|ConvertTo-Json -Compress)};return $message.result}
            if($message.method){$script:events.Add($message)}
        }
    }finally{$timeout.Dispose()}
}
function JS([string]$expression){
    $result=CDP 'Runtime.evaluate' @{expression=$expression;awaitPromise=$true;returnByValue=$true}
    if($result.exceptionDetails){throw ($result.exceptionDetails|ConvertTo-Json -Depth 20 -Compress)}
    return $result.result.value
}
$cases=@(
    @{name='memory';users=@('私は週末に読む本として「雲の駅」を選びました。','飲み物は麦茶を用意します。','さっき選んだ本の題名を教えて。','今日は机周りを掃除しました。','飲み物は変更しません。','読む本の題名と飲み物を二つとも答えて。')},
    @{name='correction';users=@('集まる場所は東の広場、時刻は午後三時です。','場所だけ西の広場へ変更します。','現在の集合場所を教えて。','時刻は午後四時半に訂正します。','場所はもう変えません。','最後の場所と時刻を確認したい。両方教えて。')},
    @{name='daily';users=@('こんにちは。今日は少し疲れています。','部屋の片付けをして疲れました。','少し座って休むことにしました。','明日の準備を一つだけ済ませたいです。簡単なものは？','持ち物を鞄にまとめておきます。','ありがとう。今日はここで終わりにします。')}
)
$report=[ordered]@{observed_at=[DateTime]::UtcNow.ToString('o');url="http://127.0.0.1:$Port";arm=$Arm;model=$model;browser=$browser;helper_pid=$ownedProcess.Id;helper_start=$ownedProcess.StartTime.ToUniversalTime().ToString('o');status='running';fixed_cases=$cases;conversations=@();mocked_requests=$false;max_new_tokens=32;source_sha256=(Get-FileHash -LiteralPath $PSCommandPath).Hash.ToLowerInvariant()}
function Save-Report{$report|ConvertTo-Json -Depth 100|Set-Content -LiteralPath $target -Encoding utf8}
Save-Report
try{
    $page=$null
    for($attempt=0;$attempt -lt 150;$attempt++){
        try{$pages=Invoke-RestMethod "http://127.0.0.1:$DebugPort/json/list" -TimeoutSec 2;$page=$pages|Where-Object type -eq 'page'|Select-Object -First 1;if($page){break}}catch{}
        Start-Sleep -Milliseconds 200
    }
    if(!$page){throw 'Dedicated helper has no exposed page; inspect the same helper'}
    $null=$socket.ConnectAsync([Uri]$page.webSocketDebuggerUrl,[Threading.CancellationToken]::None).GetAwaiter().GetResult()
    $null=CDP 'Runtime.enable' @{};$null=CDP 'Network.enable' @{};$null=CDP 'Page.enable' @{}
    $null=CDP 'Page.navigate' @{url="http://127.0.0.1:$Port"}
    $report.page=JS '(async()=>{for(let i=0;i<100;i++){if(document.querySelector("#input")&&document.querySelector("#model")?.textContent.includes("M"))return {title:document.title,model:document.querySelector("#model").textContent,footer:document.querySelector("footer").textContent,options:[...document.querySelector("#length").options].map(x=>Number(x.value)),selected:Number(document.querySelector("#length").value)};await new Promise(r=>setTimeout(r,50));}throw Error("Page not ready")})()'
    if($report.page.selected -ne 32 -or $report.page.model -notlike "*情報配置 $Arm*"){throw 'Rendered model/default length differs'}
    foreach($case in $cases){
        $reset=JS '(()=>{document.querySelector("#reset").click();return {messages:document.querySelectorAll(".message").length,input:document.querySelector("#input").value};})()'
        if($reset.messages -ne 0 -or $reset.input -ne ''){throw 'Reset retained old UI history'}
        $turns=@()
        $report.in_progress_conversation=@{name=$case.name;turns=@()};Save-Report
        foreach($text in $case.users){
            $value=ConvertTo-Json -InputObject $text -Compress
            $expression='(async()=>{const input=document.querySelector("#input");input.value='+$value+';document.querySelector("#form").requestSubmit();for(let i=0;i<300;i++){await new Promise(r=>setTimeout(r,50));if(!document.querySelector("#send").disabled){const rows=[...document.querySelectorAll(".message")].map(n=>({role:n.classList.contains("assistant")?"assistant":"user",text:[...n.childNodes].filter(x=>x.nodeType===Node.TEXT_NODE).map(x=>x.textContent).join("")}));return {messages:rows,status:document.querySelector("#status").textContent,error:document.querySelector("#status").classList.contains("error")};}}throw Error("UI timeout");})()'
            $result=JS $expression;if($result.error){throw $result.status}
            $turns+=@{user=$text;UI=$result}
            $report.in_progress_conversation.turns=$turns;Save-Report
            [PSCustomObject]@{arm=$Arm;conversation=$case.name;user=$text;reply=$result.messages[-1].text}|ConvertTo-Json -Compress|Write-Output
        }
        $report.conversations+=@{name=$case.name;reset=$reset;turns=$turns};$report.in_progress_conversation=$null;Save-Report
    }
    $requests=@($script:events|Where-Object {$_.method -eq 'Network.requestWillBeSent' -and $_.params.request.url -eq "http://127.0.0.1:$Port/api/chat"})
    $network=@()
    foreach($request in $requests){$body=CDP 'Network.getResponseBody' @{requestId=$request.params.requestId};$network+=@{request=($request.params.request.postData|ConvertFrom-Json -Depth 100);response=($body.body|ConvertFrom-Json -Depth 100)}}
    $report.network=$network
    if($network.Count -ne 18){throw 'All18 real UI requests are required'}
    for($group=0;$group -lt 3;$group++){
        $history=@()
        for($turn=0;$turn -lt 6;$turn++){
            $row=$network[6*$group+$turn];$history+=@{role='user';content=$cases[$group].users[$turn]}
            if($row.request.messages.Count -ne 2*$turn+1 -or $row.request.max_new_tokens -ne 32){throw 'Actual browser history length or cap differs'}
            for($i=0;$i -lt $history.Count;$i++){if($row.request.messages[$i].role -ne $history[$i].role -or $row.request.messages[$i].content -ne $history[$i].content){throw 'Actual browser failed to send full actual Assistant history'}}
            if($row.response.response.text -ne $report.conversations[$group].turns[$turn].UI.messages[-1].text){throw 'DOM and API replies differ'}
            $history+=@{role='assistant';content=$row.response.response.text}
        }
    }
    $report.actual_history_reset_and_DOM_API_verified=$true
    $shot=CDP 'Page.captureScreenshot' @{format='png';captureBeyondViewport=$true}
    [IO.File]::WriteAllBytes((Join-Path $root 'browser.png'),[Convert]::FromBase64String($shot.data))
    $report.status='all18_actual_browser_responses_pending_literal_review'
}catch{$report.status='failed_partial_preserved';$report.error=$_.Exception.Message;throw}
finally{
    $script:events|ConvertTo-Json -Depth 100|Set-Content -LiteralPath (Join-Path $root 'CDP_events.json') -Encoding utf8
    $report.ended_at=[DateTime]::UtcNow.ToString('o');Save-Report
    if($socket.State -eq [System.Net.WebSockets.WebSocketState]::Open){try{$null=CDP 'Browser.close' @{}}catch{}}
    $socket.Dispose()
}
