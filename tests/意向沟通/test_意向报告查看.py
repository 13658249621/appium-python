from time import sleep

import allure
from appium.webdriver.common.appiumby import AppiumBy

import pytest
from pages.主页.home_page import HomePage
from pages.我的.my_main_page import MyMainPage
from pages.意向沟通.yxgt_main_page import IntentionCommunicationMainPage
from pages.意向沟通.yxgt_report_page import IntentionCommunicationReportPage
from utils.screenshot_utils import take_screenshot

def test_意向报告查看(driver):
    home_page = HomePage(driver)
    my_main_page = MyMainPage(driver)
    main_page = IntentionCommunicationMainPage(driver)
    report_page = IntentionCommunicationReportPage(driver)

    # 1. 点击"我的tab"
    home_page.click_my_tab()
    sleep(2)
    # 2. 点击"意向沟通"
    my_main_page.click_yxgt_dynamic_bar()
    # 3. 点击"我的订单"
    main_page.click_my_order_tab()
    # 4. 点击"沟通中"
    main_page.click_communicating_tab()
    # 5. 点击"沟通完成"
    main_page.click_communicated_tab()
    # 6. 点击"筛选"
    main_page.click_filter_button()
    # 7. 点击"牛人可联系"
    main_page.click_contactable_option()
    # 8. 点击第一个牛人卡片
    main_page.click_first_candidate_card()
    # 9. 点击"查看手机"
    report_page.click_view_phone_button()
    # 10. 截图并添加到allure报告
    screenshot_path = take_screenshot(driver, test_意向报告查看.__name__)
    with allure.step("查看牛人联系方式"):
        allure.attach.file(screenshot_path, name="查看牛人联系方式", attachment_type=allure.attachment_type.PNG)
