from pages.welcome_page import WelcomePage
from pages.google_account_page import GoogleAccountPage
from pages.home_page import HomePage
from config.test_data import GOOGLE_TEST_ACCOUNT
import pytest


def test_google_login_success_and_enter_home(driver):
    welcome = WelcomePage(driver)
    google_page = GoogleAccountPage(driver)
    home = HomePage(driver)
    if home.is_loaded():
        pytest.skip("当前已在首页，跳过登录case")
    assert welcome.is_loaded(), "当前既不在首页，也不在Welcome页"
    assert welcome.is_gmail_button_displayed(), "Welcome页未显示登录按钮"
    welcome.tap_continue_with_gmail()
    assert google_page.is_loaded(), "Google账号选择页未加载"
    google_page.select_account(GOOGLE_TEST_ACCOUNT)
    assert home.is_loaded(), "登录后未进入首页"