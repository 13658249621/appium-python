import subprocess
import os
from appium import webdriver
import time
from threading import Thread, Lock

# 获取所有连接的安卓设备的 UDID
def get_connected_devices():
    adb_path = os.getenv('ANDROID_HOME', '') + '/platform-tools/adb'
    try:
        result = subprocess.run([adb_path, 'devices'], capture_output=True, text=True, check=True)
        lines = result.stdout.strip().split('\n')[1:]
        devices = []
        for line in lines:
            if line.strip():
                udid = line.split('\t')[0]
                devices.append(udid)
        print(f"get_connected_devices获取到的设备列表: {devices}")
        return devices
    except subprocess.CalledProcessError:
        print("执行 adb devices 命令出错")
        return []
    except FileNotFoundError:
        print("未找到 adb 命令，请检查 ANDROID_HOME 环境变量")
        return []

# 获取设备信息
def get_device_info(udid):
    adb_path = os.getenv('ANDROID_HOME', '') + '/platform-tools/adb'
    try:
        version_result = subprocess.run([adb_path, '-s', udid, 'shell', 'getprop', 'ro.build.version.release'],
                                        capture_output=True, text=True, check=True)
        version = version_result.stdout.strip()
        return {'udid': udid, 'version': version}
    except subprocess.CalledProcessError:
        print(f"获取设备 {udid} 信息出错")
        return None

# 创建所需的 Appium 配置
def create_desired_caps(udid, app_path, app_package, app_activity):
    device_info = get_device_info(udid)
    if device_info:
        # 获取当前脚本所在目录
        current_script_dir = os.path.dirname(os.path.abspath(__file__))
        # 获取项目根目录，假设项目根目录是当前脚本目录的上一级目录
        project_root_dir = os.path.dirname(current_script_dir)
        # 拼接 chromedriver 的绝对路径
        chromedriver_path = os.path.join(project_root_dir, 'chromedriver')
        print(f"chromedriver_path: {chromedriver_path}")
        desired_caps = {
            "platformName": "Android",
            "platformVersion": device_info['version'],
            "deviceName": udid,
            "app": app_path,
            # "appPackage": app_package,
            # "appActivity": app_activity,
            "udid": udid,
            "noReset": True,
            'chromedriverExecutable': chromedriver_path,
        }
        return desired_caps
    return None

# 设备管理器类，用于管理设备状态
class DeviceManager:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__new__(cls)
                cls._instance.__init__()
            return cls._instance

    def __init__(self):
        self.devices = get_connected_devices()
        print(f"DeviceManagerinit当前设备列表: {self.devices}")
        self.device_status = {device: 'idle' for device in self.devices}
        print(f"DeviceManagerinit当前设备状态: {self.device_status}")

    # 获取空闲设备
    def get_idle_device(self):
        with self._lock:
            for device, status in self.device_status.items():
                print(f"get_idle_device设备状态: {device} - {status}")
                if status == 'idle':
                    self.device_status[device] = 'busy'
                    return device
            return None

    # 释放设备，标记为空闲
    def release_device(self, desired_caps):
        with self._lock:
            device = desired_caps.get('udid')
            if device in self.device_status:
                self.device_status[device] = 'idle'
                print(f"设备 {device} 已释放")
                print(f"release_device设备状态: {device} - {self.device_status[device]}")
            else:
                print(f"未找到设备 {device} 的状态信息，无法释放")

