import time
from pages.form_page import FormPage

def test_login_form_validate(browser):
    login_page = FormPage(browser)
    login_page.visit()
    assert login_page.first_name.get_dom_attribute('placeholder') == 'First Name'
    assert login_page.last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert login_page.user_email.get_dom_attribute('placeholder') == 'name@example.com'
    assert login_page.user_email.get_dom_attribute('pattern') == '^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'
    login_page.btn_submit.click_force()
    assert login_page.user_form.get_dom_attribute('class') == 'was-validated'

def test_state(browser):
    form_page = FormPage(browser)
    form_page.visit()
    time.sleep(2)
    form_page.btn_state.scroll_to_element()
    form_page.btn_state.click()
    form_page.btn_NCR.click()
    time.sleep(2)

