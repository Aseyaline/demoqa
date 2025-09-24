from test_koup.herokuapp_page import HerokuAppPage
from test_koup.add_remove_elements_page import AddRemoveElementsPage


def test_btn_add(browser):
    herokuapp_page = HerokuAppPage(browser)
    add_remove_page = AddRemoveElementsPage(browser)


    herokuapp_page.visit()

    assert herokuapp_page.add_remove_elements.get_text() == 'Add/Remove Elements'
    herokuapp_page.add_remove_elements.click()
    assert herokuapp_page.get_url() == add_remove_page.get_url()

    assert add_remove_page.btn_add_element.get_text() == 'Add Element'
    assert add_remove_page.btn_add_element.get_dom_attribute('onclick') == 'addElement()'

    # Кликнуть на кнопку 4 раза
    for i in range(4):
        add_remove_page.btn_add_element.click()

    assert add_remove_page.btn_delete_element.check_count_elements(4)

    # Проверка для всех кнопок, что все они имеют надпись Delete
    for element in add_remove_page.btn_delete_element.find_elements():
        assert element.text == 'Delete'

    # Кликнуть на каждую кнопку Delete циклом while (Существует, пока условие цикла истинно - пока есть кнопки)
    while add_remove_page.btn_delete_element.exist():
        add_remove_page.btn_delete_element.click()

    # Проверка, что элементы больше не существуют
    assert not add_remove_page.btn_delete_element.exist()