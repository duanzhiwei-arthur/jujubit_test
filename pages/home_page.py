import time
from appium.webdriver.common.appiumby import AppiumBy


class HomePage:
    def __init__(self, driver):
        self.driver = driver

        # 首页/登录后有效页面特征
        self.home_locators = [
            (AppiumBy.CLASS_NAME, "android.widget.Button"),
        ]

        # 侧边栏按钮候选定位器
        self.sidebar_button_locators = [
            (AppiumBy.CLASS_NAME, "android.widget.Button"),
        ]

        # Messages 文案候选定位器
        self.messages_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Messages"),
        ]

        #inspiration 文案候选定位器
        self.inspiration_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Inspiration"),
        ]

        #creat new 文案候选定位器
        self.creat_new_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Create Now"),
        ]

        #How it works 文案候选定位器
        self.how_it_works_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "How it works"),
        ]

        #Let's Create 文案候选定位器
        self.lets_create_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Let's Create"),
        ]

        # Messages清扫按钮
        self.clean_locators = [
            (AppiumBy.CLASS_NAME, "android.widget.ImageView"),
        ]

        # 返回上一步按钮
        self.Back_locators = [
            (AppiumBy.ACCESSIBILITY_ID, "Back"),
        ]



    def _find_first(self, locators):
        for locator in locators:
            try:
                elements = self.driver.find_elements(*locator)
                if elements:
                    print(f"[HomePage] 命中 locator: {locator}")
                    return elements[0]
            except Exception:
                continue
        return None

    def _exists_once(self, locator):
        try:
            return len(self.driver.find_elements(*locator)) > 0
        except Exception:
            return False

    def is_loaded(self, timeout=0):
        print("[HomePage] 检查是否为首页")

        if timeout is None or timeout <= 0:
            for locator in self.home_locators:
                if self._exists_once(locator):
                    print(f"[HomePage] 命中 locator: {locator}")
                    return True
            return False

        start = time.time()
        interval = 0.3

        while time.time() - start < timeout:
            for locator in self.home_locators:
                if self._exists_once(locator):
                    print(f"[HomePage] 命中 locator: {locator}")
                    return True
            time.sleep(interval)

        return False

    def click_sidebar_button(self):
        print("[HomePage] 点击侧边栏按钮")
        button = self._find_first(self.sidebar_button_locators)
        if not button:
            raise Exception("未找到侧边栏按钮")
        button.click()

    def is_messages_visible(self, timeout=2):
        print("[HomePage] 检查 Messages 是否可见")

        start = time.time()
        interval = 0.3

        while time.time() - start < timeout:
            for locator in self.messages_locators:
                if self._exists_once(locator):
                    print(f"[HomePage] 命中 Messages locator: {locator}")
                    return True
            time.sleep(interval)

        return False
    

    def click_messages_button(self):
        print("[HomePage] 点击 Messages 按钮")
        button = self._find_first(self.messages_locators)
        if not button:
            raise Exception("未找到 Messages 按钮")
        button.click()

    def is_clean_visible(self, timeout=2):
        print("[HomePage] 检查清扫按钮是否可见")

        start = time.time()
        interval = 0.3

        while time.time() - start < timeout:
            for locator in self.clean_locators:
                if self._exists_once(locator):
                    print(f"[HomePage] 命中清扫按钮 locator: {locator}")
                    return True
            time.sleep(interval)

        return False
    
    def click_back_button(self):
        print("[HomePage] 点击 Back 按钮")
        button = self._find_first(self.Back_locators)
        if not button:
            raise Exception("未找到 Back 按钮")
        button.click()

    def is_inspiration_visible(self, timeout=2):
        print("[HomePage] 检查inspiration按钮是否可见")

        start = time.time()
        interval = 0.3

        while time.time() - start < timeout:
            for locator in self.inspiration_locators:
                if self._exists_once(locator):
                    print(f"[HomePage] 命中inspiration文案 locator: {locator}")
                    return True
            time.sleep(interval)

        return False
    
    def click_inspiration_button(self):
        print("[HomePage] 点击 Inspiration 按钮")
        button = self._find_first(self.inspiration_locators)
        if not button:
            raise Exception("未找到 Inspiration 按钮")
        button.click()

    def is_create_now_visible(self, timeout=2):
        print("[HomePage] 检查Create Now按钮是否可见")

        start = time.time()
        interval = 0.3

        while time.time() - start < timeout:
            for locator in self.creat_new_locators:
                if self._exists_once(locator):
                    print(f"[HomePage] 命中Create Now按钮 locator: {locator}")
                    return True
            time.sleep(interval)

        return False
    
    def click_how_it_works_button(self):
        print("[HomePage] 点击 How it works 按钮")
        button = self._find_first(self.how_it_works_locators)
        if not button:
            raise Exception("未找到 How it works 按钮")
        button.click()

    def is_lets_create_visible(self, timeout=2):
        print("[HomePage] 检查Let's Create按钮是否可见")

        start = time.time()
        interval = 0.3

        while time.time() - start < timeout:
            for locator in self.lets_create_locators:
                if self._exists_once(locator):
                    print(f"[HomePage] 命中Let's Create按钮 locator: {locator}")
                    return True
            time.sleep(interval)

        return False
    
    def click_lets_create_button(self):
        print("[HomePage] 点击 Let's Create 按钮")
        button = self._find_first(self.lets_create_locators)
        if not button:
            raise Exception("未找到 Let's Create 按钮")
        button.click()