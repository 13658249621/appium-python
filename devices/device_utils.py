import subprocess
import os
from appium import webdriver
import time
from threading import Thread

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
    def __init__(self):
        self.devices = get_connected_devices()
        self.device_status = {device: 'idle' for device in self.devices}

    # 获取空闲设备
    def get_idle_device(self):
        for device, status in self.device_status.items():
            if status == 'idle':
                self.device_status[device] = 'busy'
                return device
        return None

    # 释放设备，标记为空闲
    def release_device(self, desired_caps):
        udid = desired_caps.get('udid')
        if udid in self.device_status:
            self.device_status[udid] = 'idle'
            print(f"设备 {udid} 已释放")
        else:
            print(f"未找到设备 {udid} 的状态信息，无法释放")


# 测试用例函数
def run_test(device_udid, app_path, app_package, app_activity):
    desired_caps = create_desired_caps(device_udid, app_path, app_package, app_activity)
    if desired_caps:
        appium_server_url = 'http://localhost:4723/wd/hub'
        try:
            driver = webdriver.Remote(appium_server_url, desired_caps)
            print(f"在设备 {device_udid} 上开始测试")
            # 这里可以添加具体的测试步骤
            time.sleep(10)  # 模拟测试执行时间
            driver.quit()
            print(f"在设备 {device_udid} 上测试完成")
        except Exception as e:
            print(f"在设备 {device_udid} 上测试失败: {e}")
        finally:
            device_manager.release_device(device_udid)
    else:
        print(f"无法为设备 {device_udid} 创建所需配置")

# 主程序
if __name__ == "__main__":
    device_manager = DeviceManager()
    test_cases = 3  # 假设有 3 个测试用例
    app_path = '/Users/admin/Downloads/13.080_dev_boss_qa_debug_Arm64_dev_1308.apk'  # 替换为实际的应用路径
    # app_package = 'com.example.app'  # 替换为实际的应用包名
    # app_activity = 'com.example.app.MainActivity'  # 替换为实际的应用 Activity
    threads = []

    for _ in range(test_cases):
        device = device_manager.get_idle_device()
        if device:
            thread = Thread(target=run_test, args=(device, app_path))
            threads.append(thread)
            thread.start()
        else:
            print("没有可用的空闲设备")

    # 等待所有线程完成
    for thread in threads:
        thread.join()
