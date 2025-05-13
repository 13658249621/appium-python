import allure
from time import sleep

from pages.主页.home_page import HomePage
from pages.搜索.search_main_page import SearchMainPage
from pages.搜索.search_result_page import SearchResultPage
from pages.搜索.candidate_detail_page import CandidateDetailPage
from utils.screenshot_utils import take_screenshot
from utils.logger import get_logger
import pytest

logger = get_logger()


def test_login(driver):
    home_page = HomePage(driver)
    search_main_page = SearchMainPage(driver)
    search_result_page = SearchResultPage(driver)
    candidate_detail_page = CandidateDetailPage(driver)

    # 1. 点击搜索tab
    home_page.click_search_tab()
    logger.info("点击搜索tab")
    
    screenshot_path = take_screenshot(driver, test_login.__name__)
    with allure.step("添加截图到报告"):
        allure.attach.file(screenshot_path, name="点击搜索tab", attachment_type=allure.attachment_type.PNG)
    
    # 2. 点击搜索按钮
    search_main_page.click_search_button()
    logger.info("点击搜索按钮")
    
    screenshot_path = take_screenshot(driver, test_login.__name__)
    with allure.step("添加截图到报告"):
        allure.attach.file(screenshot_path, name="点击搜索", attachment_type=allure.attachment_type.PNG)
    
    #断言搜索结果列表中牛人卡片数量
    assert search_result_page.get_candidate_card_count() > 0, "没有搜索结果"
    
    # 3. 点击第一个牛人卡片
    search_result_page.click_first_candidate_card()
    logger.info("点击第一个牛人卡片")
    
    screenshot_path = take_screenshot(driver, test_login.__name__)
    with allure.step("添加截图到报告"):
        allure.attach.file(screenshot_path, name="点击第一个牛人卡片", attachment_type=allure.attachment_type.PNG)
    
    # 4. 点击收藏按钮
    candidate_detail_page.click_favorite_button()
    logger.info("点击收藏按钮")
    sleep(2)
    screenshot_path = take_screenshot(driver, test_login.__name__)
    with allure.step("添加截图到报告"):
        allure.attach.file(screenshot_path, name="点击收藏", attachment_type=allure.attachment_type.PNG)
