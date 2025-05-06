import os
from appium.webdriver.webdriver import WebDriver


def take_screenshot(driver: WebDriver, test_name: str, screenshot_dir: str = "app/screenshots") -> str:
    """
    截取屏幕截图并保存到指定目录
    :param driver: Appium 驱动实例
    :param test_name: 测试用例名称
    :param screenshot_dir: 截图保存目录，默认为 "app/screenshots"
    :return: 截图文件的完整路径
    """
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    screenshot_path = os.path.join(screenshot_dir, f"{test_name}.png")
    driver.get_screenshot_as_file(screenshot_path)
    return screenshot_path
