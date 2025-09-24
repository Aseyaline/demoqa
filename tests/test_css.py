from pages.text_box_page import Textbox

def test_text_box_submit(browser):
    text_box = Textbox(browser)

    text_box.visit()
    assert text_box.btn_submit.check_css('color', 'rgba(255, 255, 255, 1)')

    assert text_box.btn_submit.check_css('backgroundColor', 'rgba(0, 123, 255, 1)')
    assert text_box.btn_submit.check_css('borderColor', 'rgb(0, 123, 255)')
demoqa.com/webtables