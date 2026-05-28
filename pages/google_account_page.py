from appium.webdriver.common.appiumby import AppiumBy


class GoogleAccountPage:
    def __init__(self, driver):
        self.driver = driver

    def _exists(self, by, value):
        try:
            return len(self.driver.find_elements(by, value)) > 0
        except Exception:
            return False

    def is_account_chooser_displayed(self):
        print("[GoogleAccountPage] 检查是否为账号选择页")

        candidates = [
            (AppiumBy.XPATH, "//*[@text='Choose an account']"),
            (AppiumBy.XPATH, "//*[contains(@text,'Choose an account')]"),
            (AppiumBy.XPATH, "//*[contains(@text,'Google')]"),
        ]

        for locator in candidates:
            if self._exists(*locator):
                print(f"[GoogleAccountPage] 命中 locator: {locator}")
                return True

        return False

    def try_choose_account_by_email(self, email):
        print(f"[GoogleAccountPage] 按邮箱选择账号: {email}")
        locator = (AppiumBy.XPATH, f"//*[@text='{email}']")
        elements = self.driver.find_elements(*locator)
        if elements:
            elements[0].click()
            return True
        return False

    def choose_first_account(self):
        print("[GoogleAccountPage] 兜底选择第一个账号")
        candidates = self.driver.find_elements(
            AppiumBy.XPATH,
            "//android.widget.TextView"
        )
        for el in candidates:
            text = (el.text or "").strip()
            if "@" in text:
                el.click()
                return
        raise Exception("未找到可点击的 Google 账号")