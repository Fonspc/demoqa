from pages.text_box import TextBox


def test_text_box(browser):
    textbox = TextBox(browser)
    textbox.visit()
    textbox.name.send_keys('Max')
    textbox.current_address.send_keys('Moscow')
    textbox.btn_submit.click()
    assert textbox.name_check.get_text() == 'Name:Max'
    assert textbox.address_check.get_text() == 'Current Address :Moscow'

