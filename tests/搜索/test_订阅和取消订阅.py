from time import sleep
import pytest
from utils.logger import get_logger
from pages.主页.home_page import HomePage
from pages.搜索.search_main_page import SearchMainPage

logger = get_logger()


def test_login(driver):
    home_page = HomePage(driver)
    search_page = SearchMainPage(driver)
    
    # 1. 点击搜索tab
    home_page.click_search_tab()
    sleep(1)
    # 2. 点击我的订阅tab
    search_page.click_my_subscription_tab()
    
    # 3. 取消订阅(点击关闭订阅按钮)
    search_page.click_close_subscription_button()
    
    # 4. 确认取消订阅
    search_page.click_confirm_positive_button()
    
    # 5. 右滑到订阅区域
    search_page.swipe_right_to_left()
    # 6. 点击订阅按钮
    search_page.click_subscribe_button()
    
    # 7. 获取订阅描述文本(日志记录)
    subscription_text = search_page.get_subscription_desc_text()
    logger.info(f"获取到的文本: {subscription_text}")
    
    # 8. 点击订阅卡片
    search_page.click_subscription_card()
    
    # 9. 获取搜索框文本(日志记录)
    search_text = search_page.get_search_input_text()
    logger.info(f"获取到的文本: {search_text}")
    
    # 10. 验证搜索文本是否在订阅描述中
    assert search_text in subscription_text, f"文本不匹配: {search_text} not in {subscription_text}"
