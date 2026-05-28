import time
import pytest

from pages.welcome_page import WelcomePage
from pages.home_page import HomePage
from pages.google_account_page import GoogleAccountPage
from core.driver_factory import get_driver
from core.debug_tools import print_page_brief, dump_debug_context
from config.test_data import GOOGLE_TEST_ACCOUNT


def pytest_addoption(parser):
    parser.addoption(
        "--email",
        action="store",
        default=None,
        help="Google test account email"
    )


def detect_app_state(driver):
    """
    极速状态识别：
    不做长等待，只做瞬时判断。
    """
    google_page = GoogleAccountPage(driver)
    welcome_page = WelcomePage(driver)
    home_page = HomePage(driver)

    print("[Auth] 开始检测页面状态")

    if google_page.is_account_chooser_displayed():
        print("[Auth] 当前状态识别为: google_account_chooser")
        return "google_account_chooser"

    if welcome_page.is_login_page():
        print("[Auth] 当前状态识别为: login")
        return "login"

    if home_page.is_loaded():
        print("[Auth] 当前状态识别为: home")
        return "home"

    print("[Auth] 当前状态识别为: unknown")
    return "unknown"


def wait_until_target_state(driver, timeout=6, interval=0.5, targets=None):
    """
    快速轮询目标状态
    """
    if targets is None:
        targets = {"home"}

    start = time.time()
    while time.time() - start < timeout:
        state = detect_app_state(driver)
        if state in targets:
            print(f"[Auth] 命中目标状态: {state}")
            return state
        time.sleep(interval)

    return "unknown"


def do_google_login_flow(driver, email=None):
    welcome_page = WelcomePage(driver)
    google_page = GoogleAccountPage(driver)

    state = detect_app_state(driver)
    print(f"[Auth] 登录流程开始，当前状态: {state}")

    if state == "home":
        print("[Auth] 已在首页，无需登录")
        return "home"

    if state == "login":
        print("[Auth] 点击 Continue with Gmail")
        welcome_page.tap_continue_with_gmail()
        time.sleep(1)

    state = detect_app_state(driver)
    print(f"[Auth] 点击登录后状态: {state}")

    if state == "google_account_chooser":
        print("[Auth] 进入 Google 账号页，准备选择账号")
        if email:
            if not google_page.try_choose_account_by_email(email):
                print("[Auth] 指定邮箱未命中，兜底选择第一个账号")
                google_page.choose_first_account()
        else:
            google_page.choose_first_account()

        time.sleep(1)

    final_state = wait_until_target_state(
        driver,
        timeout=6,
        interval=0.5,
        targets={"home"}
    )
    print(f"[Auth] 登录流程结束后状态: {final_state}")

    if final_state != "home":
        print_page_brief(driver)
        dump_debug_context(driver, tag="login_flow_not_home")

    assert final_state == "home", f"登录后未进入首页，当前状态: {final_state}"
    return final_state


@pytest.fixture(scope="function")
def driver():
    print("[Fixture] 创建 driver")
    driver = get_driver()
    print("[Fixture] driver 创建成功")

    # 关键优化：关闭隐式等待，避免每次 find_element 都卡住
    try:
        driver.implicitly_wait(0)
        print("[Fixture] 已关闭隐式等待")
    except Exception as e:
        print(f"[Fixture] 设置隐式等待失败: {e}")

    try:
        print("[Fixture] 唤醒设备")
        driver.press_keycode(224)
        time.sleep(0.3)
    except Exception as e:
        print(f"[Fixture] 唤醒设备失败: {e}")

    try:
        print("[Fixture] driver.unlock()")
        driver.unlock()
        time.sleep(0.3)
    except Exception as e:
        print(f"[Fixture] driver.unlock() 失败: {e}")

    yield driver

    print("[Fixture] quit driver")
    driver.quit()


@pytest.fixture(scope="function")
def ensure_login(driver, request):
    try:
        email = request.config.getoption("email")
    except Exception as e:
        print(f"[Auth] 获取 pytest 参数 email 失败: {e}")
        email = None

    email = email or GOOGLE_TEST_ACCOUNT
    print(f"[Auth] ensure_login 使用邮箱: {email}")

    state = detect_app_state(driver)
    print(f"[Auth] 初始状态: {state}")

    if state == "home":
        print("[Auth] 已在首页，无需登录")
        return driver

    if state in ("login", "google_account_chooser"):
        do_google_login_flow(driver, email=email)
        print("[Auth] ensure_login 完成")
        return driver

    print("[Auth] 状态 unknown，打印当前页面摘要")
    print_page_brief(driver)
    dump_debug_context(driver, tag="ensure_login_unknown_state")
    pytest.fail(f"[Auth] 未知页面状态，无法继续测试。当前状态: {state}")