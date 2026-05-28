import os
from datetime import datetime


def _ensure_dir(path):
    os.makedirs(path, exist_ok=True)


def safe_get_attr(element, attr_name):
    try:
        value = element.get_attribute(attr_name)
        return value if value is not None else "null"
    except Exception:
        return "null"


def print_page_brief(driver, max_items=40):
    """
    打印当前页面元素摘要，便于快速识别当前页面状态
    """
    print("\n========== [PAGE BRIEF START] ==========")
    try:
        elements = driver.find_elements("xpath", "//*")
        for e in elements[:max_items]:
            cls = safe_get_attr(e, "class")
            text = safe_get_attr(e, "text")
            content_desc = safe_get_attr(e, "content-desc")
            resource_id = safe_get_attr(e, "resource-id")
            print(
                f"[PAGE] class={cls} | text='{text}' | content-desc='{content_desc}' | resource-id='{resource_id}'"
            )
    except Exception as ex:
        print(f"[PAGE] 无法打印页面摘要: {ex}")
    print("========== [PAGE BRIEF END] ==========\n")


def dump_debug_context(driver, tag="debug"):
    """
    保存截图和页面源码
    """
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")

    screenshot_dir = os.path.join(os.getcwd(), "screenshots")
    source_dir = os.path.join(os.getcwd(), "page_source")

    _ensure_dir(screenshot_dir)
    _ensure_dir(source_dir)

    screenshot_path = os.path.join(screenshot_dir, f"{tag}_{ts}.png")
    xml_path = os.path.join(source_dir, f"{tag}_{ts}.xml")

    try:
        driver.save_screenshot(screenshot_path)
        print(f"[DEBUG] 已保存截图: {screenshot_path}")
    except Exception as ex:
        print(f"[DEBUG] 保存截图失败: {ex}")

    try:
        source = driver.page_source
        with open(xml_path, "w", encoding="utf-8") as f:
            f.write(source)
        print(f"[DEBUG] 已保存页面源码: {xml_path}")
    except Exception as ex:
        print(f"[DEBUG] 保存页面源码失败: {ex}")