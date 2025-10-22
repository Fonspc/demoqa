from pages.base_page import BasePage
from components.components import WebElement

class Tables(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.btn_delete_row = WebElement(driver, '//span[@title="Delete"]', 'xpath')
        self.no_data = WebElement(driver, 'div.rt-noData')
        self.regform = WebElement(driver, 'body > div.fade.modal.show > div > div')
        self.regformvalid = WebElement(driver, '#userForm')
        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')
        self.btn_submit = WebElement(driver, '#submit')
        self.btn_close = WebElement(driver,
                                    'body > div.fade.modal.show > div > div > div.modal-header > button > span:nth-child(1)')
        self.btn_edit = WebElement(driver, '#edit-record-4')
        self.newstr = WebElement(driver,
                                 '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div')
        self.btn_delete = WebElement(driver, '#delete-record-4')
