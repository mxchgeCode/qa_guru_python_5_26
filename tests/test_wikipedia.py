from wikipedia_tests.model import app


def test_search():
    app.main_page.search('BrowserStack')
    app.search_results_page.assert_results_exist()


def test_return_to_main_page_from_search_results():
    app.main_page.search('Wiki')
    app.search_results_page.button_return_click()
    app.main_page.assert_title()


def test_open_settings():
    app.main_page.open_action_menu()
    app.main_page.open_settings()
    app.settings_page.assert_open()


def test_return_to_main_page_from_settings():
    app.main_page.open_action_menu()
    app.main_page.open_settings()
    app.settings_page.button_return_click()
    app.main_page.assert_title()


























