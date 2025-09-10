# 1. реализуйте тест кейс
# a. В папке тесто домашнего задания создайте файл test_visible_hw.py
# b. в файле создайте тест кейс test_visible_accordion(browser) в нем реализуйте кейс:
# i. перейти на страницу https://demoqa.com/accordian
# 1. для этого в папке pages создайте файл accordion.py
# 2. в файле реализуйте класс страницы Accordion, по аналогии с классами DemoQa и ElementsPage
# 3. Отличается только название, урл и элементы
# 4. в тестовом файле (test_visible_hw.py)
# a. импортируйте новый класс
# b. создайте объект страницы
# c. вызовите метод входа
# ii. проверьте, что элемент #section1Content > p виден
# 1. в новом классе страницы добавьте элемент с указанным локатором
# 2. в тестовом файле добавьте проверку на видимость элемента
# iii. кликните на #section1Heading
# 1. в новом классе страницы добавьте элемент с указанным локатором
# 2. в тестовом файле вызовите метод .click() для созданного элемента
# iv. После клика добавьте time.sleep(2)
# v. проверьте, что элемент #section1Content > p НЕ виден
# 1. добавьте проверку на видимость элемента и добавьте отрицание (элемент уже есть)
# 2. В файле test_visible_hw.py реализуйте второй тест кейс
# a. создайте тест кейс test_visible_accordion_default(browser) в нем реализуйте кейс:
# i. перейдите на страницу https://demoqa.com/accordian
# 1. создайте объект страницы
# 2. вызовите метод входа
# ii. проверьте, что следующие элементы по умолчанию скрыты
# 1. #section2Content > p:nth-child(1)
# 2. #section2Content > p:nth-child(2)
# 3. #section3Content > p
# 4. Для этого:
# a. Создайте каждый элемент в классе страницы
# b. в тесте вызовите проверку видимости для каждого
# c. в каждую проверку добавьте отрицание

from pages.accordion import Accordion
import time

def test_visible_accordion(browser):
    accordion_page = Accordion(browser)
    accordion_page.visit()

    assert accordion_page.text_element.visible()
    accordion_page.header_element.click()
    time.sleep(2)
    assert accordion_page.section_content_0.not_visible()


def test_visible_accordion_default(browser):
    accordion_page = Accordion(browser)
    accordion_page.visit()

    assert accordion_page.section_content_1.not_visible()
    assert accordion_page.section_content_2.not_visible()
    assert accordion_page.section_content_3.not_visible()