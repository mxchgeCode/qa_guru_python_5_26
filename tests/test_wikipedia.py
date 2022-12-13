from wikipedia_tests.model import app


def test_search():
    app.main_page.search('BrowserStack')
    app.main_page.assert_search_results_greater_than(0)


def test_open_settings():
    app.main_page.open_action_menu()
    app.main_page.open_settings()
    app.settings_page.assert_open()
















