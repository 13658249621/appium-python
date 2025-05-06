from time import sleep

import pytest
from appium import webdriver


@pytest.fixture(scope="function")
def driver():
    # 配置 Appium 服务器和设备信息
    desired_caps = {
        'platformVersion': '10',  # 设置为手机或模拟器Android版本
        'platformName': 'Android',  # 设置平台
        'deviceName': 'e5f430b',  # Android可以随便填写
        'udid': 'e5f430b',  # Android设备的唯一标识符
        # 'appPackage': 'com.hpbr.bosszhipin',  # apk包名
        # 'appActivity': '.module.main.activity.MainActivity',  # appActivity
        'app': '/Users/admin/Downloads/13.080_dev_boss_qa_debug_Arm64_dev_1308.apk',
        'unicodeKeyboard': True,
        'resetKeyboard': True,
        'noReset': True,
        'newCommandTimeout': 6000,
        'forceAppLaunch': True,
        'shouldTerminateApp': True,
        'automationName': 'UiAutomator2'
    }
    # 连接 Appium 服务器
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    yield driver
    # 测试结束后关闭驱动
    driver.quit()


def test_example(driver):
    # 这里可以编写具体的测试步骤
    # 例如查找元素并点击
    sleep(10)
    # driver.find_element("id", "com.hpbr.bosszhipin:id/btn_enter_boss").click()
    driver.find_element("id", "com.hpbr.bosszhipin:id/img_wechat_login").click()
    sleep(3)
    # 可以添加更多的断言来验证测试结果
    assert True
