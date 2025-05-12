from time import sleep

import allure
from appium.webdriver.common.appiumby import AppiumBy
from pages.主页.home_page import HomePage
from pages.我的.my_main_page import MyMainPage
from pages.意向沟通.yxgt_main_page import IntentionCommunicationMainPage
from pages.意向沟通.yxgt_report_page import IntentionCommunicationReportPage
from utils.screenshot_utils import take_screenshot



def test_login(driver):
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
    # 7. 点击"牛人电话无法接通"
    main_page.click_phone_unreachable_option()
    # 8. 点击第一个牛人卡片
    main_page.click_first_candidate_card()
    # 9. 切换上下文
    driver.switch_to.context('NATIVE_APP')
    # 10. 点击"查看简历"
    report_page.click_view_resume()
    # 11. 截图并添加到allure报告
    screenshot_path = take_screenshot(driver, test_login.__name__)
    with allure.step("添加截图到报告"):
        allure.attach.file(screenshot_path, name="查看牛人简历", attachment_type=allure.attachment_type.PNG)


