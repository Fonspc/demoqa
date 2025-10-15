from pages.modal_dialogs import ModalDialogsPage

def test_modal_elements(browser):
    modal_dialogs_page = ModalDialogsPage(browser)
    modal_dialogs_page.visit()

    assert modal_dialogs_page.btns_under_menu.check_count_elements(count = 5)


def test_navigation_dialogs(browser):
    modal_dialogs_page = ModalDialogsPage(browser)
    modal_dialogs_page.visit()

    browser.refresh()
    modal_dialogs_page.main_page.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    assert browser.current_url
    assert browser.title == 'DEMOQA'
    browser.set_window_size(1000, 1000)
