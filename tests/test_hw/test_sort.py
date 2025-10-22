from pages.tables import Tables
from selenium.webdriver.common.by import By

def test_columns_sorting(browser):
    webtables_page = Tables(browser)
    webtables_page.visit()
    headers = browser.find_elements(By.CSS_SELECTOR, "div.rt-resizable-header-content")
    assert headers
    for header in headers:
        header.click()
        parent = header.find_element(By.XPATH, "./..")
        class_value = parent.get_dom_attribute('class')
        assert ("-sort-asc" in class_value) or ("-sort-desc" in class_value), (
            f"Заголовок '{header.text}' не отсортирован после клика: {class_value}")