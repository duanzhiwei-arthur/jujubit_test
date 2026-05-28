from pages.home_page import HomePage


def test_google_login_success_and_enter_home(driver, ensure_login):
    """
    验证 Google 登录成功并进入首页/登录后有效页面
    ensure_login 已经完成登录和首次页面检查。
    这里仅做一次快速确认，避免重复等待。
    """
    home_page = HomePage(driver)
    assert home_page.is_loaded(), "登录后首页未加载成功"