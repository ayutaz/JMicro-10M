from jmicro.literary_curriculum_v2 import accepted_text,paragraphs
from test_literary_curriculum import Tokens,record


def test_generic_missing_context_old_orthography_and_personification_filters():
    for text in ['と、目を丸くしました。私は外に出ました。',
        'ふたりは部屋に戻りました。母と一緒に本を読みました。',
        '小さな木はうれしそうに大きな声を出しました。枝をひろげました。',
        '私は云いました。其の時、雨が降っていました。']:
        assert not accepted_text(text)
    text='私は部屋の窓を閉めました。雨の音が小さくなり、静かに本を読みました。'
    assert list(paragraphs(record(text),Tokens()))[0]['text']==text


def test_customer_sales_filter_keeps_objective_device_description():
    assert not accepted_text('低価格でご案内します。お客様のご要望にお応えします。')
    assert accepted_text('この機器の温度は二十度でした。温度計を使って測定しました。')
