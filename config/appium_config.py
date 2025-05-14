import os
from devices.device_utils import  create_desired_caps, DeviceManagerDB
from utils.logger import get_logger

logger = get_logger()

# Appium 服务器地址和端口
APPIUM_SERVER_URL = 'http://127.0.0.1:4725/wd/hub'


# 应用信息
APP_PATH = os.path.join(os.getcwd(), "app", "apk_files",
                        "/Users/admin/Downloads/13.080_dev_boss_qa_debug_Arm64_dev_1308.apk")
logger.info(f"APP_PATH: {APP_PATH}")
APP_PACKAGE = "com.hpbr.bosszhipin"
APP_ACTIVITY = ".module.main.activity.MainActivity"

device_manager = DeviceManagerDB()


def get_desired_caps(device_udid=None):
    if device_udid:
        return create_desired_caps(device_udid, APP_PATH, APP_PACKAGE, APP_ACTIVITY)
    device = device_manager.get_idle_device()
    logger.info(f"获取到的空闲设备: {device}")
    if device:
        return create_desired_caps(device, APP_PATH, APP_PACKAGE, APP_ACTIVITY)
    return None
