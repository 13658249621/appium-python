# Appium 自动化测试项目

本项目基于 Appium 和 pytest，面向安卓应用的自动化测试，采用页面对象模型（POM）和模块化设计，便于扩展和维护。

## 目录结构

```
├── app/                # 存放 APK 文件和截图
│   └── screenshots/    # 测试过程截图
├── config/             # 配置文件（Appium、pytest、Allure 等）
├── devices/            # 设备相关工具和 chromedriver
├── pages/              # 页面对象模型（POM），每个页面一个类
├── reports/            # 测试报告（Allure 原始结果、HTML 报告）
│   ├── allure_results/ # Allure 结果文件
│   └── html/           # HTML 格式测试报告
├── tests/              # 测试用例，按业务模块细分
│   ├── 意向沟通/      # 业务模块：意向沟通
│   └── 高搜/          # 业务模块：高搜
├── utils/              # 通用工具类（截图、ADB、日志等）
├── main.py             # Appium 脚本示例，演示设备连接与操作
├── pytest.py           # pytest 测试用例示例，含 Appium 驱动 fixture
├── pytest_html_report.py       # pytest 插件，集成截图到 HTML 报告
├── pytest_screenshot_plugin.py # pytest 插件，集成截图到 HTML 报告
├── requirements.txt    # 依赖列表
├── run_tests.sh        # 批量运行测试脚本
├── Readme.md           # 项目说明文档
```

## 主要模块说明
- **app/**：存放 APK 安装包、测试截图等资源。
- **config/**：Appium、pytest、Allure 等配置文件，便于集中管理和环境切换。
- **devices/**：设备相关工具类和 chromedriver。
- **pages/**：页面对象模型（POM），每个页面一个类，封装页面元素和操作。
- **reports/**：测试报告归档目录，含 Allure 原始结果和 HTML 报告。
- **tests/**：测试用例主目录，按业务模块细分，采用 pytest 风格。
- **utils/**：通用工具类，如截图、图像处理、ADB 操作、日志等。
- **main.py**：Appium 脚本示例，演示设备连接与简单操作。
- **pytest.py**：pytest 测试用例示例，含 Appium 驱动 fixture。
- **pytest_html_report.py / pytest_screenshot_plugin.py**：pytest 插件，集成截图到 HTML 报告。
- **requirements.txt**：依赖列表，便于环境搭建。
- **run_tests.sh**：批量运行测试脚本。

## 安装依赖
```bash
pip install -r requirements.txt
```

## 运行方式
1. 启动 Appium 服务（默认地址 http://localhost:4723/wd/hub）。
2. 运行 pytest 测试用例：
   ```bash
   pytest
   ```
3. 生成并查看 Allure 测试报告：
   ```bash
   allure generate reports/allure_results -o reports/html --clean
   allure open reports/html
   ```


---
如需扩展新业务模块或工具类，建议遵循现有目录和命名规范，保持项目结构一致性。
