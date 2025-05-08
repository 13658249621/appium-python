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


def test_login(driver):
    el1 = driver.find_element(by=AppiumBy.ID, value="com.hpbr.bosszhipin:id/tv_tab_4")
    el1.click()
    el2 = driver.find_element(by=AppiumBy.XPATH,
                              value="//android.widget.TextView[@resource-id=\"com.hpbr.bosszhipin:id/tv_title\" and @text=\"意向沟通\"]")
    el2.click()
    el3 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text=\"意向沟通\"]")
    el3.click()

    el1 = driver.find_element(by=AppiumBy.ID, value="com.hpbr.bosszhipin:id/tv_filter_item")
    el1.click()
    el2 = driver.find_element(by=AppiumBy.XPATH,
                              value="//android.widget.TextView[@resource-id=\"com.hpbr.bosszhipin:id/keywords_view_text\" and @text=\"在职-暂不考虑\"]")
    el2.click()
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(549, 1741)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(541, 958)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    sleep(1)

    el3 = driver.find_element(by=AppiumBy.XPATH,
                              value="//android.widget.TextView[@resource-id=\"com.hpbr.bosszhipin:id/keywords_view_text\" and @text=\"211院校\"]")
    el3.click()
    el4 = driver.find_element(by=AppiumBy.XPATH,
                              value="//android.widget.TextView[@resource-id=\"com.hpbr.bosszhipin:id/keywords_view_text\" and @text=\"男\"]")
    el4.click()
    el5 = driver.find_element(by=AppiumBy.ID, value="com.hpbr.bosszhipin:id/btn_confirm")
    el5.click()
    el6 = driver.find_element(by=AppiumBy.XPATH,
                              value="(//android.view.ViewGroup[@resource-id=\"com.hpbr.bosszhipin:id/cl_root\"])[1]")
    el6.click()
    sleep(1)
    screenshot_path = take_screenshot(driver, test_login.__name__)
    with allure.step("添加截图到报告"):
        allure.attach.file(screenshot_path, name="查看牛人简历", attachment_type=allure.attachment_type.PNG)
