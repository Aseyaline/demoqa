# Создаем класс страницы

from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage
from components.components import WebElement

# Класс наследуется от класса BasePage, поэтому его нужно импортировать
class DemoQA(BasePage):

# Создаем конструктор через констукцию super (в ситуациях, когда у родительского класса есть метод инициализации и
# нам нужно переопределить метод констуктора для дочернего класса)
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)

        self.icon = WebElement(driver, '#app > header > a')
        self.btn_elements = WebElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')
        self.text_check_footer = WebElement(driver, '#app > footer > span')
        self.icon_elem = WebElement(driver,'div.home-body svg > path')
        self.text_check_main = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6')