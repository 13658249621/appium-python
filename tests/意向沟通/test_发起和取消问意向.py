import pytest
from time import sleep
import allure

from pages.主页.home_page import HomePage
from pages.我的.my_main_page import MyMainPage
from pages.意向沟通.yxgt_main_page import IntentionCommunicationMainPage
from pages.意向沟通.candidate_detail_page import CandidateDetailPage
from utils.screenshot_utils import take_screenshot

@pytest.mark.smoke
def test_发起和取消问意向(driver):
    """
    测试发起和取消问意向
    """
    # 打开主页
    home_page = HomePage(driver)
    my_main_page = MyMainPage(driver)
    intention_communication_main_page = IntentionCommunicationMainPage(driver)
    candidate_detail_page = CandidateDetailPage(driver)
    
    # 点击我的tab
    home_page.click_my_tab()
    sleep(1)
    screenshot_path = take_screenshot(driver, "点击我的tab")
    with allure.step("点击我的tab"):
        allure.attach.file(screenshot_path, name="点击我的tab", attachment_type=allure.attachment_type.PNG)
    
    # 点击意向沟通
    my_main_page.click_yxgt_dynamic_bar()
    
    screenshot_path = take_screenshot(driver, "点击意向沟通")
    with allure.step("点击意向沟通"):
        allure.attach.file(screenshot_path, name="点击意向沟通", attachment_type=allure.attachment_type.PNG)

    #切换到意向沟通tab
    intention_communication_main_page.click_intention_communication_tab()

    screenshot_path = take_screenshot(driver, "切换到意向沟通tab")
    with allure.step("切换到意向沟通tab"):
        allure.attach.file(screenshot_path, name="切换到意向沟通tab", attachment_type=allure.attachment_type.PNG)

    #点击第二个牛人
    intention_communication_main_page.click_x_candidate_card(2)
    
    screenshot_path = take_screenshot(driver, "点击第二个牛人")
    with allure.step("点击第二个牛人"):
        allure.attach.file(screenshot_path, name="点击第二个牛人", attachment_type=allure.attachment_type.PNG)

    #点击发起问意向
    candidate_detail_page.click_ask_intention_button()
    
    screenshot_path = take_screenshot(driver, "点击发起问意向")
    with allure.step("点击发起问意向"):
        allure.attach.file(screenshot_path, name="点击发起问意向", attachment_type=allure.attachment_type.PNG)
        
    #点击选择职位
    candidate_detail_page.click_position_selector()
    
    screenshot_path = take_screenshot(driver, "点击选择职位")
    with allure.step("点击选择职位"):
        allure.attach.file(screenshot_path, name="点击选择职位", attachment_type=allure.attachment_type.PNG)
        
    #选择第x个职位
    candidate_detail_page.select_position(1)
    screenshot_path = take_screenshot(driver, "选择第一个职位")
    with allure.step("选择第一个职位"):
        allure.attach.file(screenshot_path, name="选择第一个职位", attachment_type=allure.attachment_type.PNG)
        
    #如果选择的职位没有变化，会停留在当前职位选择弹层，需要根据是否能获取到职位选择弹层的标题，如果能获取到该元素说明选择的职位没有变化需要手动返回
    if candidate_detail_page.get_position_select_title():
        candidate_detail_page.click_position_select_back_button()
        screenshot_path = take_screenshot(driver, "返回职位选择")
        with allure.step("返回职位选择"):
            allure.attach.file(screenshot_path, name="返回职位选择", attachment_type=allure.attachment_type.PNG)
        pass
        
    #获取问意向弹层选中的职位的名称，用于后续查看订单时进行断言
    ask_intention_position_name = candidate_detail_page.get_position_button_text()

    #点击选择注意事项，每个注意事项都点击一遍
    candidate_detail_page.select_warning_option(1)
    screenshot_path = take_screenshot(driver, "选择第一个注意事项")
    with allure.step("选择第一个注意事项"):
        allure.attach.file(screenshot_path, name="选择第一个注意事项", attachment_type=allure.attachment_type.PNG)
        
    candidate_detail_page.select_warning_option(2)
    screenshot_path = take_screenshot(driver, "选择第二个注意事项")
    with allure.step("选择第二个注意事项"):
        allure.attach.file(screenshot_path, name="选择第二个注意事项", attachment_type=allure.attachment_type.PNG)
        
    candidate_detail_page.select_warning_option(3)
    screenshot_path = take_screenshot(driver, "选择第三个注意事项")
    with allure.step("选择第三个注意事项"):
        allure.attach.file(screenshot_path, name="选择第三个注意事项", attachment_type=allure.attachment_type.PNG)

    #输入注意事项备注
    candidate_detail_page.input_warning("自动化测试输入的注意事项备注")
    screenshot_path = take_screenshot(driver, "输入注意事项备注")
    with allure.step("输入注意事项备注"):
        allure.attach.file(screenshot_path, name="输入注意事项备注", attachment_type=allure.attachment_type.PNG)

    #点击请TA沟通
    candidate_detail_page.click_contact_button()
    screenshot_path = take_screenshot(driver, "点击请TA沟通")
    with allure.step("点击请TA沟通"):
        allure.attach.file(screenshot_path, name="点击请TA沟通", attachment_type=allure.attachment_type.PNG)
    
    #发起成功后两次返回回到意向沟通tab，然后点击我的订单tab
    driver.back()
    driver.back()
    intention_communication_main_page.click_my_order_tab()
    intention_communication_main_page.swipe_order_list_container_down()
    #点击第一个订单卡片
    intention_communication_main_page.click_first_candidate_card()
    
    
