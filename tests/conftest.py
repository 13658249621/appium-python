import allure

import pytest
from appium import webdriver
from config.appium_config import APPIUM_SERVER_URL, get_desired_caps
from pytest_html_report import pytest_runtest_makereport
from utils.screenshot_utils import take_screenshot

from devices.device_utils import DeviceManager
device_manager = DeviceManager()
@pytest.fixture(scope="function")
def driver(request):
    device_udid = request.config.getoption("--device-udid")
    print(f"获取到的设备 UDID: {device_udid}")
    desired_caps = get_desired_caps(device_udid)
    if not desired_caps:
        pytest.fail("未找到可用设备")
    try:
        driver = webdriver.Remote(APPIUM_SERVER_URL, desired_caps)
        print(f"创建 driver 成功: {driver}")
        driver.implicitly_wait(10)
        yield driver
    except Exception as e:
        print(f"创建或使用 driver 时出现异常: {e}")
    finally:
        if desired_caps:
            device_manager.release_device(desired_caps)
        if 'driver' in locals():
            driver.quit()


def pytest_addoption(parser):
    print("添加命令行选项: --device-udid")
    parser.addoption("--device-udid", action="store", default=None, help="指定要使用的设备 UDID")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        try:
            driver = item.funcargs['driver']
            screenshot_path = take_screenshot(driver, item.name)
            with allure.step("添加失败截图到报告"):
                allure.attach.file(screenshot_path, name="失败截图", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print(f"截图时出现异常: {e}")

