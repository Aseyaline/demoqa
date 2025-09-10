# 2. в файле test_check_text.py реализуйте таст кейс:
# a. перейти на страницу 'https://demoqa.com/'
# b. проверить что текст в подвале == ‘© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.’

from pages.demoqa import DemoQA
from pages.elements_page import ElementsPage

def test_check_text_footer(browser):
    demo_qa_page = DemoQA(browser)
    demo_qa_page.visit()
    assert demo_qa_page.text_check_footer.get_text() == "© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED."


# 3. в файле test_check_text.py реализуйте таст кейс:
# a. перейти на страницу 'https://demoqa.com/'
# b. через кнопку перейти на страницу 'https://demoqa.com/elements'
# c. проверить что текст по центру == 'Please select an item from left to start practice.'

def test_check_text_main(browser):
    demo_qa_page = DemoQA(browser)
    demo_qa_page.visit()
    demo_qa_page.icon_elem.click()
    assert demo_qa_page.get_url() == 'https://demoqa.com/elements'
    assert demo_qa_page.text_check_main.get_text() == "Please select an item from left to start practice."

def test_page_elements(browser):
    el_page = ElementsPage(browser)

    el_page.visit()
    assert el_page.text_element.get_text() == "Please select an item from left to start practice."

def test_page_elements(browser):
    el_page = ElementsPage(browser)
    el_page.visit()

    assert el_page.icon_element.exist()
    assert el_page.btn_sidebar_first.exist()
    assert el_page.btn_sidebar_first_textbox.exist()