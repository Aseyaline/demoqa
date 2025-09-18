# 2. В папке домашних тестов создайте файл test_login_form_validate.py, в нем реализуйте тест кейс
# a. перейти на страницу https://demoqa.com/automation-practice-form
# b. проверить плейсхолдер у полей
# i. first_name
# ii. last_name
# iii. user_email - также проверьте атрибут “pattern”
# c. Сделайте попытку отправки пустой формы и проверьте наличие класса “was-validated” у элемента формы


from pages.form_page import FormPage


def test_login_form_validate(browser):
    practice_form_page = FormPage(browser)

    practice_form_page.visit()
    assert practice_form_page.first_name.get_dom_attribute('placeholder') == 'First Name'
    assert practice_form_page.last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert practice_form_page.user_email.get_dom_attribute('placeholder') == 'name@example.com'
    assert practice_form_page.user_email.get_dom_attribute('pattern') == r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'

    practice_form_page.btn_submit.scroll_to_element()
    practice_form_page.btn_submit.click()
    assert practice_form_page.user_form.get_dom_attribute('class') == 'was-validated'




