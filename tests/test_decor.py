from pages.demoqa import Demoqa
import pytest

@pytest.mark.skip
def test_decor(browser):
    demo=Demoqa(browser)
    demo.visit()

    assert demo.h5.check_count_elements(6)
    for elem in demo.h5.find_elements():
        assert elem.text!=''