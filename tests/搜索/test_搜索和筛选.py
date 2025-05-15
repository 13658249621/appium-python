import allure
from time import sleep
import pytest

from pages.主页.home_page import HomePage
from pages.搜索.search_main_page import SearchMainPage
from pages.搜索.search_result_page import SearchResultPage
from utils.screenshot_utils import take_screenshot
from utils.logger import get_logger

logger = get_logger()


def test_搜索和筛选(driver):
    # 初始化页面对象
    home_page = HomePage(driver)
    search_main_page = SearchMainPage(driver)
    search_result_page = SearchResultPage(driver)
    
    # 1. 点击搜索tab
    home_page.click_search_tab()
    logger.info("点击搜索tab")
    
    # 2. 点击搜索框
    search_main_page.click_search_box()
    logger.info("点击搜索框")
    
    # 3. 输入搜索关键词
    search_main_page.input_search_keyword("3年经验")
    logger.info("输入搜索关键词: 3年经验")
    
    # 4. 点击搜索按钮
    search_main_page.click_search_button()
    logger.info("点击搜索按钮")
    
    # 5. 点击排序筛选项
    search_result_page.click_sort_filter_option()
    logger.info("点击排序筛选项")
    
    # 6. 选择活跃优先
    search_result_page.click_active_first_option()
    logger.info("选择活跃优先")
    
    # 7. 点击学历筛选项
    search_result_page.click_education_filter_option()
    logger.info("点击学历筛选项")
    
    # 8. 选择离职-随时到岗
    search_result_page.click_available_immediately_option()
    logger.info("选择离职-随时到岗")
    
    # 9. 点击确认按钮
    search_result_page.click_confirm_button()
    logger.info("点击确认按钮")
    
    # 截图记录筛选结果
    sleep(2)
    screenshot_path = take_screenshot(driver, test_搜索和筛选.__name__)
    with allure.step("添加截图到报告"):
        allure.attach.file(screenshot_path, name="筛选结果", attachment_type=allure.attachment_type.PNG)




