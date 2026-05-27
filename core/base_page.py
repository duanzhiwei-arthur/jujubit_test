from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.timeout = timeout

    def find(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_clickable(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def click(self, locator):
        self.find_clickable(locator).click()

    def get_text(self, locator):
        return self.find(locator).text

    def get_attribute(self, locator, attr_name):
        return self.find(locator).get_attribute(attr_name)

    def is_displayed(self, locator):
        try:
            return self.find(locator).is_displayed()
        except Exception:
            return False