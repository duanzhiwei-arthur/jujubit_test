from pages.welcome_page import WelcomePage
from pages.google_account_page import GoogleAccountPage
from pages.home_page import HomePage
from config.test_data import GOOGLE_TEST_ACCOUNT


def test_google_login_success_and_enter_home(driver):
    welcome = WelcomePage(driver)
    welcome.tap_continue_with_gmail()

    google_page = GoogleAccountPage(driver)
    google_page.choose_account_by_email(GOOGLE_TEST_ACCOUNT)

    home_page = HomePage(driver)
    assert home_page.is_loaded(), "登录后未进入首页"