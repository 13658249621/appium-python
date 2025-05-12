from time import sleep
import pytest
import allure
from pages.主页.home_page import HomePage
from pages.我的.my_main_page import MyMainPage
from pages.招聘道具.recruit_props_page import RecruitPropsPage
from utils.screenshot_utils import take_screenshot

def test_login(driver):
    home_page = HomePage(driver)
    my_main_page = MyMainPage(driver)
    recruit_props_page = RecruitPropsPage(driver)

    # 1. 点击"我的tab"
    home_page.click_my_tab()
    sleep(2)
    # 2. 点击"招聘道具"
    my_main_page.click_recruit_props_button()
    # 3. 点击"我的道具"tab
    recruit_props_page.click_my_props_tab()
    # 4. 点击"已使用"tab
    recruit_props_page.click_used_tab()
    # 5. 点击"意向沟通"筛选选项
    recruit_props_page.click_intention_communication_option()
    # 6. 点击第一个"意向沟通畅聊版"道具
    recruit_props_page.click_intention_chat_prop()
    # 7. 点击"详情"按钮
    recruit_props_page.click_detail_button()
    # 8. 点击详情H5页面元素
    recruit_props_page.click_detail_h5_element()

    sleep(1)
    screenshot_path = take_screenshot(driver, test_login.__name__)
    with allure.step("添加截图到报告"):
        allure.attach.file(screenshot_path, name="查看道具详情", attachment_type=allure.attachment_type.PNG)
