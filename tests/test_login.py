# test_login.py
import os
from time import sleep

import allure

import pytest
from pages.home_page import HomePage
from pages.yxgt_main_page import YxgtMainPAge
from utils.image_math import click_by_image
from utils.screenshot_utils import take_screenshot


@pytest.mark.smoke
def test_login(driver):
    screenshot_path = take_screenshot(driver, test_login.__name__)
    with allure.step("添加截图到报告"):
        allure.attach.file(screenshot_path, name="首页截图", attachment_type=allure.attachment_type.PNG)
    # 添加断言
    assert True
    home_page = HomePage(driver)
    yxgt_main_page = YxgtMainPAge(driver)
    sleep(8)
    home_page.click_WODE_button()
    sleep(3)

    home_page.click_YXGT_button()
    sleep(3)
    #断言
    yxgt_main_page.assert_element_present(*yxgt_main_page.QuanYiMingXi_BUTTON)

    yxgt_main_page.click_quanyimingxi_button()
    sleep(3)
    screenshot_path = take_screenshot(driver, test_login.__name__)
    with allure.step("点击权益明细"):
        allure.attach.file(screenshot_path, name="点击权益明细", attachment_type=allure.attachment_type.PNG)

    click_by_image(driver, yxgt_main_page.QuGouMai_BUTTON)
    sleep(3)
    screenshot_path = take_screenshot(driver, test_login.__name__)
    with allure.step("点击去购买"):
        allure.attach.file(screenshot_path, name="点击去购买", attachment_type=allure.attachment_type.PNG)

    click_by_image(driver, yxgt_main_page.LiJiGouMai_BUTTON)
    sleep(3)
    screenshot_path = take_screenshot(driver, test_login.__name__)
    with allure.step("点击立即购买"):
        allure.attach.file(screenshot_path, name="点击立即购买", attachment_type=allure.attachment_type.PNG)
