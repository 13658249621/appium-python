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
    el4 = driver.find_element(by=AppiumBy.XPATH,
                              value="(//android.view.ViewGroup[@resource-id=\"com.hpbr.bosszhipin:id/cl_root\"])[1]")
    el4.click()
    el5 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text=\"帮我问意向\"]")
    el5.click()
    el6 = driver.find_element(by=AppiumBy.ID, value="com.hpbr.bosszhipin:id/mPositionView")
    el6.click()

