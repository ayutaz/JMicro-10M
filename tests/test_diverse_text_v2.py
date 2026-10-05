from jmicro.diverse_text_v2 import candidate


def test_rejects_missing_page_and_marketing():
    assert candidate('関西総本部では年5回程度の昇級審査を行っています。このページでは課題を一覧表としてまとめました。すると詳細ページへ移動します。',80) is None
    assert candidate('筋肉をまんべんなく鍛えると、運動を続けやすくなります。運動に興味のある人は整骨院までご連絡下さい。',80) is None


def test_retains_literal_narrative():
    text='子どもたちは学校から届いた支援物資を仕分けした。支援物資を品物ごとに分けると、必要なものを見つけやすくなった。'
    assert candidate(text,80)['text']==text
