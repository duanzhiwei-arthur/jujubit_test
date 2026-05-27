from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    SIDEBAR_BUTTON = (AppiumBy.XPATH, "//android.widget.Button")
    MESSAGES_TEXT = (AppiumBy.ACCESSIBILITY_ID, "Messages")
    INSPIRATION_TEXT = (AppiumBy.ACCESSIBILITY_ID, "Inspiration")
    CREATE_TEXT = (AppiumBy.ACCESSIBILITY_ID, "Create Now")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def is_loaded(self):
        WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(self.SIDEBAR_BUTTON)
        )
        return True

    def click_sidebar_button(self):
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.SIDEBAR_BUTTON)
        ).click()

    def is_messages_displayed(self):
        WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(self.MESSAGES_TEXT)
        )
        return True
    
    def click_sidebar_Inspiration(self):
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.INSPIRATION_TEXT)
        ).click()

    def is_create_displayed(self):
        WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(self.CREATE_TEXT)
        )
        return True