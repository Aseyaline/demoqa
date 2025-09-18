from pages.text_box_page import Textbox


def test_placeholder(browser):
    text_box_page = Textbox(browser)

    text_box_page.visit()
    assert text_box_page.full_name_form.get_dom_attribute('placeholder') == 'Full Name'