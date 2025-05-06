import subprocess
import os


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


def create_desired_caps(udid, app_path, app_package, app_activity):
    device_info = get_device_info(udid)
    if device_info:
        desired_caps = {
            "platformName": "Android",
            "platformVersion": device_info['version'],
            "deviceName": udid,
            "app": app_path,
            # "appPackage": app_package,
            # "appActivity": app_activity,
            "udid": udid,
            "noReset": True
        }
        return desired_caps
    return None
