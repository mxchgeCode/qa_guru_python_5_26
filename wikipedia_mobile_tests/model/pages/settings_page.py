import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene.support.shared import browser
from selene.support.conditions import have, be


class SettingsPage():
    title_settings = (AppiumBy.CLASS_NAME, 'android.widget.TextView')
    button_return = (AppiumBy.CLASS_NAME, 'android.widget.ImageButton')

    def assert_open(self):
        with allure.step('Проверяем, что открылась страница Settings'):
            browser.all(self.title_settings).element_by(have.text('Settings')).should(be.visible)

    def button_return_click(self):
        with allure.step('Нажимаем кнопку возврата на предыдущую страницу'):
            browser.element(self.button_return).click()















