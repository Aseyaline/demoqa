from pages.base_page import BasePage
from components.components import WebElement


class Textbox(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)

        self.full_name_form = WebElement(driver, '#userName')
        self.current_address_form = WebElement(driver, '#currentAddress')
        self.btn_submit = WebElement(driver, '#submit')

        # Output elements
        self.output_full_name_form = WebElement(driver, '#name')
        self.output_current_address_form = WebElement(driver, '//form/div[6]/div/p[2]', 'xpath')