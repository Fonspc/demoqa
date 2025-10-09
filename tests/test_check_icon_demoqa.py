
from pages.demoqa import Demoqa

def test_check_icon(browser):
    demo_qa_page = Demoqa(browser)
    demo_qa_page.visit()
    demo_qa_page.icon.click()
    assert demo_qa_page.equal_url()
    assert demo_qa_page.icon.exist()





# def test_icon_exist(browser):
#     demo_qa_page = Demoqa(browser)
#     demo_qa_page.visit()
#     demo_qa_page.click_on_the_icon()
#     assert demo_qa_page.equal_url()
#     assert demo_qa_page.icon.exist()


