from pages.base_page import BasePage
from components.components import WebElement

class TextBox(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)
        self.name = WebElement(driver, '#userName')
        self.name_check = WebElement(self.driver, '#name')
        self.current_address = WebElement(self.driver, '#currentAddress')
        self.address_check = WebElement(self.driver, '#output > div> #currentAddress')
        self.submit = WebElement(self.driver, '#submit')