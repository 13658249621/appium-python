import subprocess

# 请根据实际情况修改 adb 的路径
adb_path = '/Users/admin/Library/Android/sdk/platform-tools/adb'

try:
    # 执行 adb devices 命令获取设备列表
    devices_result = subprocess.run([adb_path, 'devices'], capture_output=True, text=True, check=True)
    devices_output = devices_result.stdout.strip().split('\n')[1:]  # 去除标题行

    deviceinfo = []
    for line in devices_output:
        if line:
            udid = line.split('\t')[0]
            # 执行 adb 命令获取安卓版本
            version_result = subprocess.run([adb_path, '-s', udid, 'shell', 'getprop', 'ro.build.version.release'],
                                            capture_output=True, text=True, check=True)
            version = version_result.stdout.strip()
            deviceinfo.append({'udid': udid, 'version': version})

    # 打印设备信息
    for info in deviceinfo:
        print(f"UDID: {info['udid']}, Android Version: {info['version']}")

except subprocess.CalledProcessError as e:
    print(f"命令执行出错: {e.stderr}")
except FileNotFoundError:
    print(f"未找到指定路径的 adb 命令，请检查路径: {adb_path}")
