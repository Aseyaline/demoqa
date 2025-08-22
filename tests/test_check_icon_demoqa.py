from pages.demoqa import DemoQA

def test_icon_exist(browser):
    demo_qa_page = DemoQA(browser)
    demo_qa_page.visit()
    demo_qa_page.icon.click()
    assert demo_qa_page.equal_url()
    assert demo_qa_page.icon.exist()
