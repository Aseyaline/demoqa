from pages.base_page import BasePage
from components.components import WebElement

class Accordion(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.text_element = WebElement(driver, "#section1Content > p")
        self.header_element = WebElement(driver, "#section1Heading")
        self.section_content_0 = WebElement(driver, "#section1Content > p")

# default = not visible
        self.section_content_1 = WebElement(driver, "#section2Content > p:nth-child(1)")
        self.section_content_2 = WebElement(driver, "#section2Content > p:nth-child(2)")
        self.section_content_3 = WebElement(driver, "#section3Content > p")