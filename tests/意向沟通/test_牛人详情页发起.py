from time import sleep
import pytest
from pages.主页.home_page import HomePage
from pages.我的.my_main_page import MyMainPage
from pages.意向沟通.yxgt_main_page import IntentionCommunicationMainPage
from pages.意向沟通.candidate_detail_page import CandidateDetailPage


def test_login(driver):
    home_page = HomePage(driver)
    my_main_page = MyMainPage(driver)
    main_page = IntentionCommunicationMainPage(driver)
    candidate_page = CandidateDetailPage(driver)

    # 1. 点击"我的tab"
    home_page.click_my_tab()
    sleep(2)
    # 2. 点击"意向沟通"动态条
    my_main_page.click_yxgt_dynamic_bar()
    # 3. 点击"意向沟通"tab
    main_page.click_yxgt_tab()
    # 4. 点击第一个牛人卡片
    main_page.click_first_candidate_root()
    # 5. 点击"帮我问意向"按钮
    candidate_page.click_ask_intention_button()
    # 6. 点击职位选择控件
    candidate_page.click_position_selector()

