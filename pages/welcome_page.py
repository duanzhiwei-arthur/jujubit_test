from appium.webdriver.common.appiumby import AppiumBy


class WelcomePage:
    def __init__(self, driver):
        self.driver = driver
        self.login_button_locator = (
            AppiumBy.XPATH,
            "//*[@content-desc='Continue with Gmail']"
        )

    def is_login_page(self):
        print("[WelcomePage] 检查是否为登录页")
        try:
            elements = self.driver.find_elements(*self.login_button_locator)
            if elements:
                print(f"[WelcomePage] 命中登录按钮 locator: {self.login_button_locator}")
                return True
            return False
        except Exception:
            return False

    def tap_continue_with_gmail(self):
        print(f"[WelcomePage] 点击 Google/Gmail 登录按钮: {self.login_button_locator}")
        elements = self.driver.find_elements(*self.login_button_locator)
        if not elements:
            raise Exception("未找到 Continue with Gmail 按钮")
        elements[0].click()