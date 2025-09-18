# 1. В папке домашних тестов создайте файл test_text_box.py, в нем реализуйте тест кейс
# a. перейти на страницу https://demoqa.com/text-box
# b. записать в поля Full Name, Current Address произвольный текст
# c. нажать на кнопку submit
# d. проверить, что снизу появились 2 элемента с нашим текстом
# i. * сравнение и ввод текста, реализовать через переменную


from pages.text_box_page import Textbox


def test_text_box(browser):
    text_box_page = Textbox(browser)

    # переменные:
    full_name = "MY NAME"
    current_address = "MY ADDRESS"

    text_box_page.visit()
    text_box_page.full_name_form.send_keys(full_name)
    text_box_page.current_address_form.send_keys(current_address)
    text_box_page.btn_submit.click()
    assert text_box_page.output_full_name_form.visible()
    assert full_name in text_box_page.output_full_name_form.get_text()
    assert text_box_page.output_current_address_form.visible()
    assert current_address in text_box_page.output_current_address_form.get_text()