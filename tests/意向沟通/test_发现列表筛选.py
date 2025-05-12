from time import sleep

import allure
from pages.主页.home_page import HomePage
from pages.我的.my_main_page import MyMainPage
from pages.意向沟通.yxgt_main_page import IntentionCommunicationMainPage
from utils.screenshot_utils import take_screenshot
import pytest

def test_login(driver):
    home_page = HomePage(driver)
    my_main_page = MyMainPage(driver)
    main_page = IntentionCommunicationMainPage(driver)

    # 1. 点击"我的tab"
    home_page.click_my_tab()
    sleep(2)
    # 2. 点击"意向沟通"动态条
    my_main_page.click_yxgt_dynamic_bar()
    # 3. 点击"意向沟通"tab
    main_page.click_yxgt_tab()
    # 4. 点击筛选项按钮
    main_page.click_filter_item_button()
    # 5. 点击"在职-暂不考虑"筛选项
    main_page.click_employed_not_considering_option()
    # 6. 从下往上滑动列表
    main_page.swipe_list_up()
    sleep(1)
    # 7. 点击"211院校"筛选项
    main_page.click_top_university_option()
    # 8. 点击"男"筛选项
    main_page.click_male_option()
    # 9. 点击确认按钮
    main_page.click_confirm_button()
    # 10. 点击第一个牛人卡片
    main_page.click_first_candidate_root()
    sleep(1)
    # 11. 截图并添加到allure报告
    screenshot_path = take_screenshot(driver, test_login.__name__)
    with allure.step("添加截图到报告"):
        allure.attach.file(screenshot_path, name="查看牛人简历", attachment_type=allure.attachment_type.PNG)
