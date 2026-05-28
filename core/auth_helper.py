from pages.home_page import HomePage
from pages.welcome_page import WelcomePage
from pages.google_account_page import GoogleAccountPage


class AuthHelper:
    def __init__(self, driver):
        self.driver = driver
        self.home_page = HomePage(driver)
        self.welcome_page = WelcomePage(driver)
        self.google_account_page = GoogleAccountPage(driver)

    def ensure_login(self, email=None):
        """
        确保已登录并进入首页
        """
        if self.home_page.is_loaded():
            print("【Auth】已在首页，跳过登录")
            return

        print("【Auth】未在首页，开始登录流程")

        if self.welcome_page.is_loaded():
            print("【Auth】当前在欢迎页，点击 Continue with Gmail")
            self.welcome_page.tap_continue_with_gmail()
        else:
            raise AssertionError("【Auth】当前既不在首页，也不在欢迎页，无法执行登录")

        if self.google_account_page.is_loaded():
            print("【Auth】检测到 Google 账号页")
            if email:
                print(f"【Auth】按邮箱选择账号: {email}")
                self.google_account_page.choose_account_by_email(email)
            else:
                print("【Auth】未传入邮箱，默认选择第一个账号")
                self.google_account_page.choose_first_account()
        else:
            print("【Auth】未检测到 Google 账号页，继续等待首页加载")

        assert self.home_page.is_loaded(), "【Auth】登录后首页未加载成功"
        print("【Auth】登录成功，已进入首页")