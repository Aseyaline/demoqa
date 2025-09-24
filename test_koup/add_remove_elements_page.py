from pages.base_page import BasePage
from components.components import WebElement


class AddRemoveElementsPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://the-internet.herokuapp.com/add_remove_elements'
        super().__init__(driver, self.base_url)

        self.btn_add_element = WebElement(driver, '#content > div > button')

        # Delete
        self.btn_delete_element = WebElement(driver, '#elements > button')

        # self.delete_element_2 = WebElement(driver, '#elements > button:nth-child(2)')
        # self.delete_element_3 = WebElement(driver, '#elements > button:nth-child(3)')
        # self.delete_element_4 = WebElement(driver, '#elements > button:nth-child(4)')