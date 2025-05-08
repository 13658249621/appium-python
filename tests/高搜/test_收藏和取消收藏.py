import os
from time import sleep

import allure
from appium.webdriver.common.appiumby import AppiumBy

import pytest
from pages.home_page import HomePage
from pages.yxgt_main_page import YxgtMainPAge
from utils.image_math import click_by_image
from utils.screenshot_utils import take_screenshot



def test_login(driver):
    # 添加断言
    assert True
    home_page = HomePage(driver)
    yxgt_main_page = YxgtMainPAge(driver)

    el1 = driver.find_element(by=AppiumBy.ID, value="com.hpbr.bosszhipin:id/tv_tab_2")
    el1.click()

    screenshot_path = take_screenshot(driver, test_login.__name__)
    with allure.step("添加截图到报告"):
        allure.attach.file(screenshot_path, name="点击搜索tab", attachment_type=allure.attachment_type.PNG)

    els2 = driver.find_elements(by=AppiumBy.ID, value="com.hpbr.bosszhipin:id/tv_search_action")
    els2[0].click()

    screenshot_path = take_screenshot(driver, test_login.__name__)
    with allure.step("添加截图到报告"):
        allure.attach.file(screenshot_path, name="点击搜索", attachment_type=allure.attachment_type.PNG)

    el2 = driver.find_element(by=AppiumBy.XPATH,
                              value="(//android.view.ViewGroup[@resource-id=\"com.hpbr.bosszhipin:id/cl_search_card\"])[1]")
    el2.click()

    screenshot_path = take_screenshot(driver, test_login.__name__)
    with allure.step("添加截图到报告"):
        allure.attach.file(screenshot_path, name="点击第一个牛人卡片", attachment_type=allure.attachment_type.PNG)

    el3 = driver.find_element(by=AppiumBy.XPATH,
                              value="(//android.widget.ImageView[@resource-id=\"com.hpbr.bosszhipin:id/iv_icon\"])[1]")
    el3.click()

    screenshot_path = take_screenshot(driver, test_login.__name__)
    with allure.step("添加截图到报告"):
        allure.attach.file(screenshot_path, name="点击收藏", attachment_type=allure.attachment_type.PNG)
