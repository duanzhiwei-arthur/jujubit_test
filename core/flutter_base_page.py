class FlutterBasePage:
    def __init__(self, driver):
        self.driver = driver

    def by_value_key(self, key):
        """
        返回 Flutter Key 定位器
        实际使用时根据你接入的 flutter finder 库写法调整
        """
        return {"finderType": "ByValueKey", "keyValueString": key}

    def tap_by_key(self, key):
        finder = self.by_value_key(key)
        self.driver.execute_script("flutter:tap", finder)

    def enter_text_by_key(self, key, text):
        finder = self.by_value_key(key)
        self.driver.execute_script("flutter:tap", finder)
        self.driver.execute_script("flutter:enterText", text)

    def wait_for_element_by_key(self, key, timeout=10):
        finder = self.by_value_key(key)
        self.driver.execute_script("flutter:waitFor", finder, timeout)

    def get_text_by_key(self, key):
        finder = self.by_value_key(key)
        return self.driver.execute_script("flutter:getText", finder)