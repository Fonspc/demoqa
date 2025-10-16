from pages.koup import Koup
from pages.koup_add import KoupAdd
import time


def test_koup_add(browser):
    koup_page = Koup(browser)
    koup_add = KoupAdd(browser)
    koup_page.visit()

    assert koup_page.link_add.get_text() == 'Add/Remove Elements'
    koup_page.link_add.click()
    assert koup_add.equal_url()

    assert koup_add.btn_add.get_text() == 'Add Element'

    assert koup_add.btn_add.get_dom_attribute('onclick') == 'addElement()'

    # Клик 4 раза
    for i in range(4):
        koup_add.btn_add.click()

    assert koup_add.btn_delete.check_count_elements(4)

    # Проверка для всех элементов
    for element in koup_add.btn_delete.find_elements():
        assert element.text == 'Delete'

    # Проверка только для первого элемента
    assert koup_add.btn_delete.get_text() == 'Delete'

    # Клик на каждую кнопку Delete
    while koup_add.btn_delete.exists():
        koup_add.btn_delete.click()

    assert not koup_add.btn_delete.exists()
    time.sleep(2)