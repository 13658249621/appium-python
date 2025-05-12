import allure
from time import sleep
import pytest

from pages.主页.home_page import HomePage
from pages.搜索.search_main_page import SearchMainPage
from pages.搜索.search_result_page import SearchResultPage
from pages.搜索.candidate_detail_page import CandidateDetailPage
from pages.搜索.forward_page import ColleagueSelectPage
from utils.screenshot_utils import take_screenshot
from utils.logger import get_logger

logger = get_logger()


def test_login(driver):
    # 初始化页面对象
    home_page = HomePage(driver)
    search_main_page = SearchMainPage(driver)
    search_result_page = SearchResultPage(driver)
    candidate_detail_page = CandidateDetailPage(driver)
    forward_page = ColleagueSelectPage(driver)
    
    # 1. 点击搜索tab
    home_page.click_search_tab()
    logger.info("点击搜索tab")
    
    # 2. 点击我的订阅tab
    search_main_page.click_my_subscription_tab()
    logger.info("点击我的订阅tab")
    
    # 3. 点击第一个牛人卡片
    search_result_page.click_first_candidate_card()
    logger.info("点击第一个牛人卡片")
    
    # 4. 点击转发操作父容器
    candidate_detail_page.click_forward_parent()
    logger.info("点击转发操作父容器")
    
    # 5. 点击选择其他按钮
    candidate_detail_page.click_select_other_button()
    logger.info("点击选择其他按钮")
    
    # 6. 切换到原生应用上下文
    forward_page.switch_to_native_context()
    logger.info("切换到原生应用上下文")
    
    # 7. 点击同事搜索框
    forward_page.click_colleague_search_box()
    logger.info("点击同事搜索框")
    
    # 8. 输入同事搜索关键词
    forward_page.input_colleague_keyword("马")
    logger.info("输入同事搜索关键词: 马")
    
    # 截图记录搜索结果
    sleep(2)
    screenshot_path = take_screenshot(driver, test_login.__name__)
    with allure.step("添加截图到报告"):
        allure.attach.file(screenshot_path, name="同事搜索结果", attachment_type=allure.attachment_type.PNG)





