import os
from time import sleep

import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

import pytest
from pages.home_page import HomePage
from pages.yxgt_main_page import YxgtMainPAge
from utils.image_math import click_by_image
from utils.screenshot_utils import take_screenshot


@pytest.mark.smoke
def test_login(driver):
    el1 = driver.find_element(by=AppiumBy.ID, value="com.hpbr.bosszhipin:id/tv_tab_4")
    el1.click()
    sleep(2)
    el2 = driver.find_element(by=AppiumBy.XPATH,
                              value="//android.widget.TextView[@text=\"招聘道具\"]")
    el2.click()
    el3 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text=\"我的道具\"]")
    el3.click()
    el4 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text=\"已使用\"]")
    el4.click()
    el5 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text=\"意向沟通\"]")
    el5.click()
    el6 = driver.find_element(by=AppiumBy.XPATH, value="(//android.widget.TextView[@text=\"意向沟通畅聊版\"])[1]")
    el6.click()
    el7 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text=\"详情\"]")
    el7.click()
    el8 = driver.find_element(by=AppiumBy.XPATH,
                              value="//android.view.View[@resource-id=\"app\"]/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View[2]")
    el8.click()

    sleep(1)
    screenshot_path = take_screenshot(driver, test_login.__name__)
    with allure.step("添加截图到报告"):
        allure.attach.file(screenshot_path, name="查看牛人简历", attachment_type=allure.attachment_type.PNG)
