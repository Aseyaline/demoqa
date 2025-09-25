from pages.base_page import BasePage
from components.components import WebElement


class WebTables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.table = WebElement(driver, 'div.rt-table > div.rt-tbody')
        self.no_rows_found = WebElement(driver, 'div.rt-noData')

        # hw
        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.dialog_registration_form = WebElement(driver, 'body > div.fade.modal.show > div')
        self.btn_edit = WebElement(driver, '#edit-record-1')
        self.btn_delete = WebElement(driver, '#delete-record-1')

        #Registration Form
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')
        self.btn_submit = WebElement(driver, '#submit')

        self.rows = WebElement(driver, 'span.select-wrap.-pageSizeOptions > select')
        self.btn_previous = WebElement(driver, 'div.-previous > button')
        self.btn_next = WebElement(driver, 'div.-next > button')

        self.total_pages = WebElement(driver, 'div.-center > span.-pageInfo > span')
        self.page_of = WebElement(driver, 'div.-center > span.-pageInfo > div > input[type=number]')

