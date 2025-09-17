# 1. создайте тестовый файл test_page_dialogs.py реализуйте тест кейс test_modal_elements()
# a. перейти на страницу https://demoqa.com/modal-dialogs
# i. в каталоге pages создайте класс страницы modal_dialogs.py
# ii. в тестовом файле создайте объект новой страницы
# iii. от объекта вызовите метод входа на страницу
# b. проверить, что кнопок подменю, на странице - 5 шт
# i. в классе страницы создайте элемент с не уникальным локатором, подходящим под все кнопки
# ii. в тестовом файле обратитесь к объекту страницы - к элементу - вызовите метод проверки кол-ва элементов
# 2. в том-же файле реализуйте тест кейс test_navigation_modal()
# a. перейти на страницу https://demoqa.com/modal-dialogs
# i. класс страницы уже создан
# ii. создайте объект новой страницы
# iii. от объекта вызовите метод входа на страницу
# b. обновить страницу
# c. перейти на главную страницу через иконку
# i. в файле класса страницы создайте элемент иконки
# d. сделать шаг назад стрелкой браузера
# e. установить размеры экрана 900х400
# f. сделать шаг вперед стрелкой браузера
# g. вызвать проверку урла на главной странице
# h. проверить title на главной
# i. вернуть размеры экрана по умолчанию 1000x1000


from pages.modal_dialogs import Modal_dialogs
import time


def test_modal_elements(browser):
     modal_dialogs = Modal_dialogs(browser)

     modal_dialogs.visit()
     assert modal_dialogs.submenu.check_count_elements(count=5)


def test_navigation_modal(browser):
     modal_dialogs = Modal_dialogs(browser)

     modal_dialogs.visit()
     browser.refresh()
     modal_dialogs.home_icon.click()
     browser.back()
     browser.set_window_size(width=900, height=400)
     browser.forward()
     time.sleep(2)
     assert browser.current_url == 'https://demoqa.com/'
     assert browser.title == 'DEMOQA'
     browser.set_window_size(width=1000, height=1000)