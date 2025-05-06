from time import sleep
import warnings
from urllib3.exceptions import NotOpenSSLWarning
from appium import webdriver
from selenium.webdriver.chrome.options import Options


# 忽略 urllib3 的 NotOpenSSLWarning 警告
warnings.filterwarnings("ignore", category=NotOpenSSLWarning)
options = Options()
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

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

try:
    # 这里可以编写具体的测试步骤
    sleep(10)
    # driver.find_element("id", "com.hpbr.bosszhipin:id/btn_enter_boss").click()
    driver.find_element("id", "com.hpbr.bosszhipin:id/img_wechat_login").click()
    sleep(3)
    pass
finally:
    driver.quit()
