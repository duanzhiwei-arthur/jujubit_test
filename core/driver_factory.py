import yaml
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions


def load_config(platform: str):
    config_file = f"config/{platform}.yaml"
    with open(config_file, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_driver(platform="android"):
    config = load_config(platform)
    server_url = config["serverUrl"]

    if config["platformName"].lower() == "android":
        caps = {
            "platformName": "Android",
            "deviceName": config["deviceName"],
            "automationName": config.get("automationName", "UiAutomator2"),
            "appPackage": config["appPackage"],
            "appActivity": config["appActivity"],
            "noReset": config.get("noReset", True),
            "newCommandTimeout": config.get("newCommandTimeout", 300),
        }
        options = UiAutomator2Options().load_capabilities(caps)

    elif config["platformName"].lower() == "ios":
        caps = {
            "platformName": "iOS",
            "deviceName": config["deviceName"],
            "platformVersion": config["platformVersion"],
            "automationName": config.get("automationName", "XCUITest"),
            "udid": config["udid"],
            "bundleId": config["bundleId"],
            "noReset": config.get("noReset", True),
            "newCommandTimeout": config.get("newCommandTimeout", 300),
            "xcodeOrgId": config["xcodeOrgId"],
            "xcodeSigningId": config.get("xcodeSigningId", "iPhone Developer"),
            "updatedWDABundleId": config["updatedWDABundleId"],
        }
        options = XCUITestOptions().load_capabilities(caps)

    else:
        raise ValueError(f"不支持的平台: {config['platformName']}")

    driver = webdriver.Remote(server_url, options=options)
    driver.implicitly_wait(10)
    return driver