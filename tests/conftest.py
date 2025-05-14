"""
conftest.py 说明：
1. pytest 会自动发现并加载每个测试目录及其父目录下名为 conftest.py 的文件。
2. conftest.py 中定义的 fixture、hook、插件等内容会自动生效，无需手动 import。
3. 其作用范围为所在目录及所有子目录，实现作用域隔离和资源共享。
4. 如果不是命名为 conftest.py，pytest 不会自动识别和加载其中的 fixture 和 hook，必须手动 import。
"""
import allure

import pytest
from appium import webdriver
from config.appium_config import APPIUM_SERVER_URL, get_desired_caps
from utils.screenshot_utils import take_screenshot
from utils.logger import get_logger
from devices.device_utils import DeviceManagerDB

device_manager = DeviceManagerDB()
logger = get_logger()

@pytest.fixture(scope="session")
def device_udid():
    device_manager = DeviceManagerDB()
    device = device_manager.get_idle_device()
    logger.info(f"选择到的空闲设备: {device}")
    if not device:
        pytest.fail("没有可用的设备")
    yield device
    # session 结束时释放设备
    logger.info(f"释放设备: {device}")
    device_manager.release_device(device['udid'])

@pytest.fixture(scope="function")
def driver(device_udid):
    logger.info(f"创建 driver，使用设备: {device_udid}")
    device_manager = DeviceManagerDB()
    desired_caps = get_desired_caps(device_udid['udid'])
    driver = None
    try:
        driver = webdriver.Remote(APPIUM_SERVER_URL, desired_caps)
        driver.implicitly_wait(10)
        yield driver
    except Exception as e:
        logger.error(f"driver fixture发生异常: {e}")
        raise
    finally:
        if driver:
            logger.info(f"销毁 driver，使用设备: {device_udid}")
            driver.quit()
        # 无论如何都释放设备
        device_manager.release_device(device_udid['udid'])

def pytest_addoption(parser):
    logger.info("添加命令行选项: --device-udid")
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
            logger.error(f"截图时出现异常: {e}")

