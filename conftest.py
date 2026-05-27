import pytest
from core.driver_factory import get_driver


def pytest_addoption(parser):
    parser.addoption(
        "--platform",
        action="store",
        default="android",
        help="运行平台: android 或 ios"
    )


@pytest.fixture(scope="function")
def driver(request):
    platform = request.config.getoption("--platform")
    d = get_driver(platform)
    yield d
    d.quit()