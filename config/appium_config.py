# appium_config.py
import os

# Appium 服务器地址和端口
APPIUM_SERVER_URL = 'http://localhost:4723/wd/hub'

# 设备和应用配置
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
