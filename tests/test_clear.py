from pages.text_box_page import Textbox
import time

def test_clear(browser):
    text_box_page = Textbox(browser)

    text_box_page.visit()
    text_box_page.full_name_form.send_keys('MY NAME')
    time.sleep(2)
    text_box_page.full_name_form.clear()
    time.sleep(2)
    assert text_box_page.full_name_form.get_text() == ''
