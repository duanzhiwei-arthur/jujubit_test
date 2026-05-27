from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from core.base_page import BasePage


class GoogleAccountPage(BasePage):
    ALL_TEXT_VIEWS = (AppiumBy.CLASS_NAME, "android.widget.TextView")

    def account_locator_by_email(self, email):
        return (
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().text("{email}")'
        )

    def wait_for_account_page_loaded(self):
        WebDriverWait(self.driver, self.timeout).until(
            lambda d: len(d.find_elements(*self.ALL_TEXT_VIEWS)) > 0
        )
        return True

    def choose_account_by_email(self, email):
        self.wait_for_account_page_loaded()
        locator = self.account_locator_by_email(email)
        self.click(locator)