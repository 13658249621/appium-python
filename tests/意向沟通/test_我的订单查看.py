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
    el3 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text=\"我的订单\"]")
    el3.click()

    el7 = driver.find_element(by=AppiumBy.XPATH,
                              value="//android.widget.TextView[@resource-id=\"com.hpbr.bosszhipin:id/tv_title\" and @text=\"沟通中\"]")
    el7.click()
    el8 = driver.find_element(by=AppiumBy.XPATH,
                              value="//android.widget.TextView[@resource-id=\"com.hpbr.bosszhipin:id/tv_title\" and @text=\"沟通完成\"]")
    el8.click()
    el9 = driver.find_element(by=AppiumBy.ID, value="com.hpbr.bosszhipin:id/tv_filter")
    el9.click()
    el10 = driver.find_element(by=AppiumBy.XPATH,
                               value="//android.widget.TextView[@resource-id=\"com.hpbr.bosszhipin:id/tv_title\" and @text=\"牛人电话无法接通\"]")
    el10.click()
    el11 = driver.find_element(by=AppiumBy.XPATH,
                               value="//androidx.recyclerview.widget.RecyclerView[@resource-id=\"com.hpbr.bosszhipin:id/rv_list\"]/android.view.ViewGroup[1]")
    el11.click()
    driver.switch_to.context('NATIVE_APP')
    els2 = driver.find_elements(by=AppiumBy.XPATH, value="//android.widget.TextView[@text=\"查看简历\"]")
    els2[0].click()
    screenshot_path = take_screenshot(driver, test_login.__name__)
    with allure.step("添加截图到报告"):
        allure.attach.file(screenshot_path, name="查看牛人简历", attachment_type=allure.attachment_type.PNG)


