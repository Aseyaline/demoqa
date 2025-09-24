# 2. В папке домашних тестов создайте файл test_login_form_validate.py, в нем реализуйте тест кейс
# a. перейти на страницу https://demoqa.com/automation-practice-form
# b. проверить плейсхолдер у полей
# i. first_name
# ii. last_name
# iii. user_email - также проверьте атрибут “pattern”
# c. Сделайте попытку отправки пустой формы и проверьте наличие класса “was-validated” у элемента формы

from selenium.webdriver import Keys
from pages.form_page import FormPage
import time

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

# Несколько способов выбрать элемент из выпадающего списка:
# 1. Способ через конструкцию '//*[contains(text(), "NCR")]'

def test_state(browser):
    form_page = FormPage(browser)

    form_page.visit()
    time.sleep(2)
    form_page.btn_state.scroll_to_element()
    form_page.btn_state.click()
    form_page.btn_NCR.click()
    time.sleep(2)

# 2. Способ через написание текста в поле и нажатия Enter, если набранный текст соответвует существующему элементу в списке.

def test_state_2(browser):
    form_page = FormPage(browser)

    form_page.visit()
    time.sleep(2)
    form_page.btn_state.scroll_to_element()
    time.sleep(2)
    form_page.inp_state.send_keys('NCR')
    form_page.inp_state.send_keys(Keys.ENTER)
    time.sleep(2)

# 3. Способ через склик по выпадающему списку и с помощью клавиш-стрелок выбор нужного элемента.

def test_state_3(browser):
    form_page = FormPage(browser)

    form_page.visit()
    time.sleep(2)
    form_page.btn_state.scroll_to_element()
    time.sleep(2)
    form_page.btn_state.click()
    form_page.inp_state.send_keys(Keys.PAGE_UP)
    form_page.inp_state.send_keys(Keys.ENTER)
    time.sleep(2)




