from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from core.base_page import BasePage


class HomePage(BasePage):
    # ===== 首页唯一标识 =====
    # 注意：这里是示例 locator，你需要根据真实页面调整
    SIDEBAR_BUTTON = (AppiumBy.XPATH, "//android.widget.Button")
    # ===== 侧边栏相关元素 =====
    MESSAGES_TEXT = (AppiumBy.ACCESSIBILITY_ID, "Messages")
    INSPIRATION_TEXT = (AppiumBy.ACCESSIBILITY_ID, "Inspiration")
    CREATE_TEXT = (AppiumBy.ACCESSIBILITY_ID, "Create Now")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
    
    def is_loaded(self):
        """
        判断首页是否加载完成
        """
        return self.is_displayed(self.SIDEBAR_BUTTON, timeout=8)
    def is_sidebar_button_displayed(self):
        """
        判断侧边栏按钮是否显示
        """
        return self.is_displayed(self.SIDEBAR_BUTTON, timeout=5)
    def click_sidebar_button(self):
        """
        点击侧边栏按钮
        """
        self.click(self.SIDEBAR_BUTTON)
    def is_messages_displayed(self):
        """
        判断 Messages 是否显示
        """
        return self.is_displayed(self.MESSAGES_TEXT, timeout=5)
    def is_inspiration_displayed(self):
        """
        判断 Inspiration 是否显示
        """
        return self.is_displayed(self.INSPIRATION_TEXT, timeout=5)
    def click_sidebar_Inspiration(self):
        """
        点击侧边栏中的 Inspiration
        保持和你测试代码一致
        """
        self.click(self.INSPIRATION_TEXT)
    def is_create_displayed(self):
        """
        判断 Create Now 是否显示
        """
        return self.is_displayed(self.CREATE_TEXT, timeout=8)