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
    el1 = driver.find_element(by=AppiumBy.ID, value="com.hpbr.bosszhipin:id/tv_tab_2")
    el1.click()
    el2 = driver.find_element(by=AppiumBy.XPATH,
                              value="//android.widget.TextView[@resource-id=\"com.hpbr.bosszhipin:id/tv_tab_name\" and @text=\"我的订阅\"]")
    el2.click()
    el3 = driver.find_element(by=AppiumBy.ID, value="com.hpbr.bosszhipin:id/iv_subscribe_close")
    el3.click()
    el21 = driver.find_element(by=AppiumBy.ID, value="com.hpbr.bosszhipin:id/tv_positive")
    el21.click()
    sleep(1)
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(922, 623)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(328, 614)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

    el22 = driver.find_element(by=AppiumBy.XPATH,
                               value='(//android.widget.Button[@resource-id="com.hpbr.bosszhipin:id/btn_subscribe"])')
    el22.click()


    text_el1 = driver.find_element(by=AppiumBy.XPATH,
                                   value='//android.widget.TextView[@resource-id="com.hpbr.bosszhipin:id/tv_subscribe_desc"]')
    text1 = text_el1.get_attribute('text')
    print(f"获取到的文本: {text1}")

    cards = driver.find_elements(AppiumBy.XPATH,
                                 '(//android.view.ViewGroup[@resource-id="com.hpbr.bosszhipin:id/cl_subscribe_card"])')
    cards[0].click()


    text_el2 = driver.find_element(by=AppiumBy.ID, value='com.hpbr.bosszhipin:id/et_input')
    text2 = text_el2.get_attribute('text')
    print(f"获取到的文本: {text2}")
    assert text2 in text1, f"文本不匹配: {text2} not in {text1}"
