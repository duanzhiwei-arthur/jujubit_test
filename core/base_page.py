from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def find_element(self, locator, timeout=None):
        timeout = timeout or self.timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_elements(self, locator, timeout=None):
        timeout = timeout or self.timeout
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        return self.driver.find_elements(*locator)

    def click(self, locator, timeout=None):
        timeout = timeout or self.timeout
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def is_displayed(self, locator, timeout=5):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return element.is_displayed()
        except Exception:
            return False

    def is_visible(self, locator, timeout=5):
        return self.is_displayed(locator, timeout=timeout)

    def is_present(self, locator, timeout=3):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except Exception:
            return False

    def get_text(self, locator, timeout=None):
        timeout = timeout or self.timeout
        return self.find_element(locator, timeout).text

    def save_screenshot(self, file_path):
        return self.driver.save_screenshot(file_path)

    def get_page_source(self):
        return self.driver.page_source