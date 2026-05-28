from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.timeout = timeout

    def find(self, locator, timeout=None):
        wait_timeout = timeout if timeout is not None else self.timeout
        return WebDriverWait(self.driver, wait_timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_clickable(self, locator, timeout=None):
        wait_timeout = timeout if timeout is not None else self.timeout
        return WebDriverWait(self.driver, wait_timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def click(self, locator, timeout=None):
        self.find_clickable(locator, timeout).click()

    def get_text(self, locator, timeout=None):
        return self.find(locator, timeout).text

    def get_attribute(self, locator, attr_name, timeout=None):
        return self.find(locator, timeout).get_attribute(attr_name)

    def is_displayed(self, locator, timeout=None):
        try:
            return self.find(locator, timeout).is_displayed()
        except (TimeoutException, NoSuchElementException):
            return False

    def input_text(self, locator, text, timeout=10):
        element = self.find(locator, timeout)
        element.clear()
        element.send_keys(text)

    def is_element_exist(self, locator, timeout=3):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except (TimeoutException, NoSuchElementException):
            return False