
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
    el4 = driver.find_element(by=AppiumBy.ID, value="com.hpbr.bosszhipin:id/tv_tab_2")
    el4.click()
    el5 = driver.find_element(by=AppiumBy.XPATH,
                              value="//android.widget.TextView[@resource-id=\"com.hpbr.bosszhipin:id/tv_tab_name\" and @text=\"我的订阅\"]")
    el5.click()
    el6 = driver.find_element(by=AppiumBy.XPATH,
                              value="(//android.view.ViewGroup[@resource-id=\"com.hpbr.bosszhipin:id/cl_search_card\"])[1]")
    el6.click()
    el7 = driver.find_element(by=AppiumBy.XPATH,
                              value="(//android.view.ViewGroup[@resource-id=\"com.hpbr.bosszhipin:id/cl_parent\"])[2]")
    el7.click()
    el8 = driver.find_element(by=AppiumBy.XPATH,
                              value="//android.widget.TextView[@resource-id=\"com.hpbr.bosszhipin:id/forwardName\" and @text=\"选择其他\"]")
    el8.click()
    driver.switch_to.context('NATIVE_APP')
    el11 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text=\"搜索你的同事（姓名/职位/邮箱)\"]")
    el11.click()
    el12 = driver.find_element(by=AppiumBy.ID, value="com.hpbr.bosszhipin:id/et_input")
    el12.send_keys("马")
    # el13 = driver.find_element(by=AppiumBy.XPATH,
    #                            value="//android.widget.ListView[@resource-id=\"com.hpbr.bosszhipin:id/listview\"]/android.view.ViewGroup[1]")
    # el13.click()
    # el14 = driver.find_element(by=AppiumBy.ID, value="com.hpbr.bosszhipin:id/btn_send")
    # el14.click()
    # el15 = driver.find_element(by=AppiumBy.ID, value="com.hpbr.bosszhipin:id/iv_back")
    # el15.click()
    # el16 = driver.find_element(by=AppiumBy.ID, value="com.hpbr.bosszhipin:id/iv_back")
    # el16.click()
    # el17 = driver.find_element(by=AppiumBy.ID, value="com.hpbr.bosszhipin:id/tv_tab_3")
    # el17.click()
    # el18 = driver.find_element(by=AppiumBy.XPATH,
    #                            value="//android.widget.TextView[@resource-id=\"com.hpbr.bosszhipin:id/tv_title\" and @text=\"全部\"]")
    # el18.click()





