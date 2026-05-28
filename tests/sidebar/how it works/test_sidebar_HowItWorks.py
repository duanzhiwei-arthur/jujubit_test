from pages.home_page import HomePage


def test_click_sidebar_button_should_show_messages(driver, ensure_login):
    """
    点击侧边栏按钮，进入侧边栏，点击how it works按钮，进入how it works页面，在返回
    """
    home_page = HomePage(driver)

    # 确保首页已加载
    assert home_page.is_loaded(timeout=1), "首页未加载成功"

    # 点击侧边栏按钮
    home_page.click_sidebar_button()

    # 断言 Messages 出现
    assert home_page.is_messages_visible(timeout=2), "点击侧边栏后未出现 Messages"

     # 点击how it works按钮
    home_page.click_how_it_works_button()

    # 断言 Let's Create 出现
    assert home_page.is_lets_create_visible(timeout=2), "点击how it works后未出现Let's Create按钮"

    # 点击let's create按钮
    home_page.click_lets_create_button()

    # 断言 侧边栏按钮 出现
    assert home_page.is_loaded(timeout=2), "点击let's create按钮后未返回首页"