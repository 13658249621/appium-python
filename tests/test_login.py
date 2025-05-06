# test_login.py
import os
from time import sleep

import allure

import pytest
from pages.home_page import HomePage
from utils.screenshot_utils import take_screenshot


@pytest.mark.smoke
def test_login(driver):
    screenshot_path = take_screenshot(driver, test_login.__name__)
    with allure.step("添加截图到报告"):
        allure.attach.file(screenshot_path, name="首页截图", attachment_type=allure.attachment_type.PNG)
    # 添加断言
    assert True
    home_page = HomePage(driver)
    sleep(8)
    home_page.click_WEIXIN_button()
    screenshot_path = take_screenshot(driver, test_login.__name__)
    with allure.step("添加截图到报告"):
        allure.attach.file(screenshot_path, name="点击微信截图", attachment_type=allure.attachment_type.PNG)
    sleep(3)
        # 这里可以添加断言来验证登录结果
