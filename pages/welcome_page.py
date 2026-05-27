from appium.webdriver.common.appiumby import AppiumBy
from core.base_page import BasePage


class WelcomePage(BasePage):
    BTN_CONTINUE_WITH_GMAIL = (
        AppiumBy.ACCESSIBILITY_ID,
        "Continue with Gmail"
    )
    BTN_CONTINUE_AS_GUEST = (
        AppiumBy.ACCESSIBILITY_ID,
        "Continue as a guest"
    )

    def is_loaded(self):
        return self.is_gmail_button_displayed()

    def is_gmail_button_displayed(self):
        return self.is_displayed(self.BTN_CONTINUE_WITH_GMAIL)

    def is_guest_button_displayed(self):
        return self.is_displayed(self.BTN_CONTINUE_AS_GUEST)

    def tap_continue_with_gmail(self):
        self.click(self.BTN_CONTINUE_WITH_GMAIL)

    def tap_continue_as_guest(self):
        self.click(self.BTN_CONTINUE_AS_GUEST)