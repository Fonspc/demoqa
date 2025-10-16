from pages.tables import Tables
import time

def test_webtables(browser):
    webtable = Tables(browser)

    webtable.visit()
    webtable.btn_add.click()
    time.sleep(2)
    assert not webtable.regformvalid.get_dom_attribute('class') == 'was-validated'
    webtable.btn_submit.click()
    assert webtable.regformvalid.get_dom_attribute('class') == 'was-validated'
    webtable.btn_close.click()

    webtable.btn_add.click()
    webtable.first_name.send_keys("Max")
    webtable.last_name.send_keys("Bongo")
    webtable.email.send_keys("uyth@mail.ru")
    webtable.age.send_keys("34")
    webtable.salary.send_keys("2146")
    webtable.department.send_keys("Department")
    webtable.btn_submit.click()
    time.sleep(1)
    assert webtable.newstr.exist()

    webtable.btn_edit.click()
    time.sleep(1)
    webtable.first_name.clear()
    time.sleep(1)
    webtable.first_name.send_keys("Petr")
    webtable.btn_submit.click()
    time.sleep(2)

    webtable.btn_delete.click()
    assert not webtable.newstr.get_dom_attribute('class') == 'rt-tr -odd'