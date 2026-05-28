from pages.home_page import HomePage


def test_click_sidebar_button_should_show_messages(driver, ensure_login):
    """
    点击侧边栏按钮，进入侧边栏，点击inspiration按钮，进入inspiration页面，在返回
    """
    home_page = HomePage(driver)

    # 确保首页已加载
    assert home_page.is_loaded(timeout=1), "首页未加载成功"

    # 点击侧边栏按钮
    home_page.click_sidebar_button()

    # 断言 Messages 出现
    assert home_page.is_messages_visible(timeout=2), "点击侧边栏后未出现 Messages"

     # 点击inspiration按钮
    home_page.click_inspiration_button()

    # 断言 Create Now 出现
    assert home_page.is_create_now_visible(timeout=2), "点击inspiration后未出现Create Now按钮"

    # 点击返回按钮
    home_page.click_sidebar_button()

    # 断言 messages 出现
    assert home_page.is_messages_visible(timeout=2), "点击返回按钮后未出现messages文案"
