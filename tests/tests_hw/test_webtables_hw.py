# 1. Автоматизируйте тест кейс, страница https://demoqa.com/webtables
# a. на странице имеется кнопка Add
# b. по клику на кнопку Add открывается диалоговое окно
# c. в диалоге нельзя сохранить пустую форму
# d. если заполнить все поля и нажать на кнопку Submit
# i. диалог закрывается
# ii. в таблицу добавляется новая запись с введенными данными
# e. если кликнуть на карандаш на строке записи
# i. открывается диалог с введенными данными
# f. если изменить имя и сохранить то в таблице обновятся данные
# g. если нажать на корзину в строке записи - запись удаляется


from pages.web_tables_page import WebTables
from selenium.webdriver.common.keys import Keys


def test_webtables_hw(browser):
    web_tables = WebTables(browser)

    web_tables.visit()

    web_tables.btn_add.click()
    assert web_tables.dialog_registration_form.exist()

    web_tables.btn_submit.click()
    assert web_tables.dialog_registration_form.exist()

    web_tables.first_name.send_keys('test')
    web_tables.last_name.send_keys('test-test')
    web_tables.email.send_keys('test@test.com')
    web_tables.age.send_keys('19')
    web_tables.salary.send_keys('100000')
    web_tables.department.send_keys('QA')
    web_tables.btn_submit.click()
    assert not web_tables.dialog_registration_form.exist()

    assert 'test' in web_tables.table.get_text()

    web_tables.btn_edit.click()
    assert web_tables.dialog_registration_form.exist()
    assert web_tables.first_name.get_dom_attribute('value') == 'Cierra'

    web_tables.first_name.send_keys('Newname')
    web_tables.btn_submit.click()
    assert 'Newname' in web_tables.table.get_text()
    web_tables.btn_delete.click()
    assert not 'Newname' in web_tables.table.get_text()


# 2. * Автоматизируйте тест кейс, страница https://demoqa.com/webtables
# a. предусловия
# i. открыта страница
# ii. кол-во строк в таблице установлено 5
# b. тест кейс
# i. кнопки Next и Previous заблокированы (по клику ничего не происходит и имеют атрибут disabled)
# ii. если добавить в таблицу еще 3 записи то:
# 1. появляется 2-я страница (of 2)
# 2. кнопка Next становится доступной
# iii. если кликнуть по кнопке Next то открывается 2-я страница
# iv. если кликнуть по кнопке Previous то открывается 1-я страница


def test_webtables_hw_2(browser):
    # Предусловие:
    web_tables = WebTables(browser)
    web_tables.visit()
    web_tables.rows.scroll_to_element()
    web_tables.rows.click()
    web_tables.rows.send_keys(Keys.ARROW_UP + Keys.ENTER)
    # testcase
    assert web_tables.btn_previous.get_dom_attribute('disabled')
    assert web_tables.btn_next.get_dom_attribute('disabled')
    assert web_tables.total_pages.get_text() == '1'

    for number in range(1,4):

        web_tables.btn_add.click()
        web_tables.first_name.send_keys(f'test{number}')
        web_tables.last_name.send_keys('test-test')
        web_tables.email.send_keys('test@test.com')
        web_tables.age.send_keys('19')
        web_tables.salary.send_keys('100000')
        web_tables.department.send_keys('QA')
        web_tables.btn_submit.click()

    assert 'test1' in web_tables.table.get_text()
    assert 'test2' in web_tables.table.get_text()

    assert web_tables.total_pages.get_text() == '2'
    assert not web_tables.btn_next.get_dom_attribute('disabled')

    web_tables.btn_next.click()
    assert 'test3' in web_tables.table.get_text()
    assert  web_tables.page_of.get_dom_attribute('value') == '2'

    assert not web_tables.btn_previous.get_dom_attribute('disabled')
    web_tables.btn_previous.click()
    assert  web_tables.page_of.get_dom_attribute('value') == '1'