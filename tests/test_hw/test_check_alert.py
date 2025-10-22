from pages.alerts import Alerts
import time

def test_timer(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    assert alert_page.btn_timer.exist()
    alert_page.btn_timer.click()
    time.sleep(5)
    assert alert_page.alert()
    alert_page.alert().accept()

