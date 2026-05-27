from pages.home_page import HomePage


def test_click_sidebar_button_should_show_messages(driver):
    """
    点击侧边栏按钮，断言出现 Messages 文案
    """
    home_page = HomePage(driver)

    # 确保首页已加载
    assert home_page.is_loaded(), "首页未加载成功"

    # 点击侧边栏按钮
    home_page.click_sidebar_button()

    # 断言 Messages 文案出现
    assert home_page.is_messages_displayed(), "点击侧边栏后未出现 Messages 文案"

    # 点击侧边栏中的 Inspiration 文案
    home_page.click_sidebar_Inspiration()

    # 断言 Create Now 文案出现
    assert home_page.is_create_displayed(), "点击侧边栏后未出现 Create Now 文案"