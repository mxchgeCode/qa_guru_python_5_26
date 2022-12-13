import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene.support.shared import browser
from selene.support.conditions import have, be


class MainPage():
    field_search_init = (AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")
    field_search_do = (AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")
    search_results = (AppiumBy.CLASS_NAME, "android.widget.TextView")
    button_action_menu = (AppiumBy.ID, "org.wikipedia.alpha:id/menu_overflow_button")
    button_settings = (AppiumBy.ID, "org.wikipedia.alpha:id/explore_overflow_settings")

    def search(self, value):
        with allure.step('Выполняем поиск'):
            browser.element(self.field_search_init).click()
            browser.element(self.field_search_do).type(value)

    def assert_search_results_greater_than(self, value):
        with allure.step('Выполняем проверку результатов поиска'):
            browser.all(self.search_results).should(have.size_greater_than(value))

    def open_action_menu(self):
        with allure.step('Открываем меню действий'):
            browser.element(self.button_action_menu).click()

    def open_settings(self):
        with allure.step('Выбираем в меню пункт Settings'):
            browser.element(self.button_settings).click()

