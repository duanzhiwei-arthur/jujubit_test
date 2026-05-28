from pages.home_page import HomePage


def test_click_sidebar_button_should_show_messages(driver, ensure_login):
    """
    点击messages 进入messages在返回
    """
    home_page = HomePage(driver)

     # 点击message按钮
    home_page.click_messages_button()

    # 断言 Messages 出现
    assert home_page.is_clean_visible(timeout=2), "点击messages后未出现清扫按钮"

    # 点击返回按钮
    home_page.click_back_button()

    # 断言 inspiration 出现
    assert home_page.is_inspiration_visible(timeout=2), "点击返回按钮后未出现inspiration按钮"


     # 点击关闭侧边栏按钮
    home_page.click_sidebar_button()