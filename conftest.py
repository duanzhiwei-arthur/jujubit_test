import pytest
from core.driver_factory import get_driver
from core.auth_helper import AuthHelper
from config.test_data import GOOGLE_TEST_ACCOUNT
from pages.home_page import HomePage
import os
from datetime import datetime
import allure
import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--email",
        action="store",
        default=None,
        help="Google account email for login"
    )


@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def ensure_login(driver, request):
    email = request.config.getoption("--email") or GOOGLE_TEST_ACCOUNT
    auth = AuthHelper(driver)
    auth.ensure_login(email=email)
    home = HomePage(driver)
    assert home.is_loaded(), "ensure_login后仍未进入首页"
    return driver

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    用例执行完成后：
    - 如果失败，自动截图
    - 自动附加错误堆栈到 Allure
    """
    outcome = yield
    report = outcome.get_result()
    # 只在测试步骤失败时截图，不在 setup/teardown 阶段处理
    if report.when != "call":
        return
    # 把 report 挂到 item 上，其他地方如果要用也方便
    setattr(item, "rep_call", report)
    if report.failed:
        driver = item.funcargs.get("driver")
        if driver is None:
            return
        screenshot_dir = os.path.join(os.getcwd(), "screenshots")
        os.makedirs(screenshot_dir, exist_ok=True)
        file_name = f"{item.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        file_path = os.path.join(screenshot_dir, file_name)
        try:
            driver.save_screenshot(file_path)
            with open(file_path, "rb") as f:
                allure.attach(
                    f.read(),
                    name=f"{item.name}_failure_screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
            allure.attach(
                str(report.longrepr),
                name=f"{item.name}_error_trace",
                attachment_type=allure.attachment_type.TEXT
            )
            print(f"[HOOK] 已保存失败截图: {file_path}")
        except Exception as e:
            print(f"[HOOK] 失败截图保存异常: {e}")