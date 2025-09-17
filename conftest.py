import pytest
from selenium import webdriver

# Выносим драйвер с помощью декоратора @pytest.fixture, создаем функцию, в которую передаем драйвер,
# конструкция yield нужна, чтобы его использовать, и закрываем драйвер

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    driver.set_window_size(1000, 1000)
    yield driver
    driver.quit()