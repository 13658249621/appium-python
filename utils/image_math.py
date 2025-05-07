import requests
import json

# 定义常量
URL = "http://127.0.0.1:5000/upload"


def main():
    # 这里假设我们可以获取到模板和目标的二进制数据
    # 实际中可以通过文件读取等方式
    with open("/Users/admin/Downloads/权益明细.jpg", 'rb') as f1, open("/Users/admin/Downloads/去购买.jpg", 'rb') as f2:
        template_binary = f1.read()
        target_binary = f2.read()

    # 构造请求文件数据
    files = {
        'file1': ('tem.jpg', template_binary, 'image/jpeg'),
        'file2': ('tar.png', target_binary, 'image/jpeg')
    }

    # 发起请求
    response = requests.post(URL, files=files)

    # 检查响应状态
    if response.status_code != 200:
        raise Exception(f"Unexpected code {response}")

    # 输出响应数据
    print(response.text)


def image_match(driver, target):
    print("开始进行图片匹配2")
    # 获取模板的二进制截图数据
    template_binary = driver.get_screenshot_as_png()
    try:
        # 读取目标图片文件
        with open(target, 'rb') as f:
            target_binary = f.read()
    except FileNotFoundError:
        print(f"未找到目标图片文件: {target}")
        return None

    # 构造请求文件数据
    files = {
        'file1': ('tem.jpg', template_binary, 'image/jpeg'),
        'file2': ('tar.png', target_binary, 'image/jpeg')
    }

    # 发起请求
    print("开始发送请求")
    response = requests.post(URL, files=files)

    # 检查响应状态
    if response.status_code != 200:
        raise Exception(f"Unexpected code {response}")

    try:
        # 解析 JSON 数据
        print("开始解析响应数据")
        clean_text = response.text.strip()
        print("响应内容:", clean_text)
        json_data = json.loads(clean_text)
        print(json_data)
        pos = json_data.get('pos')
        print(pos)
        result = [pos[0], pos[1]]
        return result
    except json.JSONDecodeError:
        print("响应内容不是有效的 JSON 格式，响应内容为:", response.text)
        return None


def click_by_image(driver, target):
    print("开始进行图片匹配1")
    result = image_match(driver, target)
    if result:
        print("点击位置:", result)
        driver.tap([(result[0], result[1])], 200)
        return True
    return False


if __name__ == "__main__":
    main()

