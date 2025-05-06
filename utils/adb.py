import subprocess


class AdbDeviceUtils:
    def __init__(self, adb_path):
        self.adb_path = adb_path

    def run_adb_command(self, command):
        try:
            result = subprocess.run([self.adb_path] + command, capture_output=True, text=True, check=True)
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            print(f"命令执行出错: {e.stderr}")
            return None
        except FileNotFoundError:
            print(f"未找到指定路径的 adb 命令，请检查路径: {self.adb_path}")
            return None

    def get_connected_devices(self):
        output = self.run_adb_command(['devices'])
        if output is None:
            return []
        lines = output.split('\n')[1:]  # 去除标题行
        devices = []
        for line in lines:
            if line.strip():
                udid = line.split('\t')[0]
                devices.append(udid)
        return devices

    def get_device_android_version(self, udid):
        version = self.run_adb_command(['-s', udid, 'shell', 'getprop', 'ro.build.version.release'])
        return version

    def get_all_device_info(self):
        devices = self.get_connected_devices()
        device_info = []
        for udid in devices:
            version = self.get_device_android_version(udid)
            if version is not None:
                device_info.append({'udid': udid, 'version': version})
        return device_info


if __name__ == "__main__":
    # 请根据实际情况修改 adb 的路径
    adb_path = '/Users/admin/Library/Android/sdk/platform-tools/adb'
    utils = AdbDeviceUtils(adb_path)
    device_info = utils.get_all_device_info()
    for info in device_info:
        print(f"UDID: {info['udid']}, Android Version: {info['version']}")
