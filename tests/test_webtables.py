from pages.web_tables_page import WebTables


def test_web_tables(browser):
    web_tables = WebTables(browser)

    web_tables.visit()

    assert not web_tables.no_rows_found.exists()

