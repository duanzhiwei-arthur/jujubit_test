from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from core.base_page import BasePage


class GoogleAccountPage(BasePage):
    """
    Google 账号选择页
    """

    ALL_TEXT_VIEWS = (AppiumBy.CLASS_NAME, "android.widget.TextView")

    def account_locator_by_email(self, email):
        return (
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().text("{email}")'
        )

    def is_loaded(self, timeout=10):
        """
        判断 Google 账号页是否加载完成
        这里用页面上出现 TextView 作为宽松判断
        如果后续你能拿到更精准的标题 locator，建议替换
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: len(d.find_elements(*self.ALL_TEXT_VIEWS)) > 0
            )
            return True
        except TimeoutException:
            return False

    def wait_for_account_page_loaded(self, timeout=10):
        """
        等待 Google 账号页加载完成
        """
        WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.find_elements(*self.ALL_TEXT_VIEWS)) > 0
        )
        return True

    def choose_account_by_email(self, email):
        """
        按邮箱选择账号
        """
        self.wait_for_account_page_loaded()
        locator = self.account_locator_by_email(email)
        self.click(locator)

    def choose_first_account(self):
        """
        兜底：选择第一个可见文本账号
        注意：这个方法不够精准，只建议临时使用
        """
        self.wait_for_account_page_loaded()
        elements = self.driver.find_elements(*self.ALL_TEXT_VIEWS)
        for element in elements:
            text = element.text.strip()
            if "@" in text:
                element.click()
                return
        raise AssertionError("Google 账号页中未找到可点击的邮箱账号")