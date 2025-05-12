import pytest
import os
from pytest_html import extras

#没有调用了
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call":
        # 获取截图目录
        screenshot_dir = os.path.join(os.getcwd(), "screenshots")
        if os.path.exists(screenshot_dir):
            # 查找与当前测试用例相关的截图文件
            for root, dirs, files in os.walk(screenshot_dir):
                for file in files:
                    if item.name in file:
                        screenshot_path = os.path.join(root, file)
                        # 将截图添加到报告中
                        report.extra.append(extras.image(screenshot_path))
