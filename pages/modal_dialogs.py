from components.components import WebElement
from pages.base_page import BasePage

class ModalDialogsPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btns_under_menu = WebElement(driver,'#app > div > div > div > div:nth-child(1) > div > div > div:nth-child(3) > div > ul > li')
        self.main_page = WebElement(driver, '#app > header > a')

        self.btn_small_modal = WebElement(driver, '#showSmallModal')
        self.btn_large_modal = WebElement(driver, '#showLargeModal')
        self.btn_close_small = WebElement(driver, '#closeSmallModal')
        self.btn_close_large = WebElement(driver, '#closeLargeModal')
        self.modal_small = WebElement(driver, '#example-modal-sizes-title-sm')
        self.modal_large = WebElement(driver, '#example-modal-sizes-title-lg')





