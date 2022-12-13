import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene.support.shared import browser
from selene.support.conditions import have, be


class SettingsPage():
    title_settings = (AppiumBy.CLASS_NAME, "android.widget.TextView")

     def assert_open(self):
        with allure.step('Проверяем, что открылась страница Settings'):
            browser.all(self.title_settings).element_by(have.text('Settings')).should(be.visible)



