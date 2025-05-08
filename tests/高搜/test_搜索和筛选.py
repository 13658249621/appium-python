
import os
from time import sleep

import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains

import pytest
from pages.home_page import HomePage
from pages.yxgt_main_page import YxgtMainPAge
from utils.image_math import click_by_image
from utils.screenshot_utils import take_screenshot




def test_login(driver):
    el24 = driver.find_element(by=AppiumBy.ID, value="com.hpbr.bosszhipin:id/tv_tab_2")
    el24.click()
    el25 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text=\"请输入公司/行业/技能等\"]")
    el25.click()
    el26 = driver.find_element(by=AppiumBy.ID, value="com.hpbr.bosszhipin:id/et_input")
    el26.send_keys("3年经验")
    el27 = driver.find_element(by=AppiumBy.ID, value="com.hpbr.bosszhipin:id/tv_search_action")
    el27.click()
    el28 = driver.find_element(by=AppiumBy.XPATH,
                               value="//android.widget.TextView[@resource-id=\"com.hpbr.bosszhipin:id/tv_display_name\" and @text=\"排序\"]")
    el28.click()
    el29 = driver.find_element(by=AppiumBy.XPATH,
                               value="//android.widget.TextView[@resource-id=\"com.hpbr.bosszhipin:id/tv_content\" and @text=\"活跃优先\"]")
    el29.click()
    el30 = driver.find_element(by=AppiumBy.XPATH,
                               value="//android.widget.TextView[@resource-id=\"com.hpbr.bosszhipin:id/tv_display_name\" and @text=\"学历\"]")
    el30.click()
    el31 = driver.find_element(by=AppiumBy.XPATH,
                               value="//android.widget.TextView[@resource-id=\"com.hpbr.bosszhipin:id/keywords_view_text\" and @text=\"离职-随时到岗\"]")
    el31.click()
    el32 = driver.find_element(by=AppiumBy.ID, value="com.hpbr.bosszhipin:id/btn_confirm")
    el32.click()




