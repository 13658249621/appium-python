import pytest

from pages.消息.message_main_page import MessageMainPage
from pages.消息.互动.意向沟通.intention_filter_page import IntentionFilterPage
from pages.消息.互动.意向沟通.intention_communication_page import IntentionCommunicationPage
from pages.主页.home_page import HomePage
import allure
from time import sleep

from utils.screenshot_utils import take_screenshot


@pytest.mark.smoke
def test_intention_communication(driver):
    """测试互动-意向沟通页面的主要流程"""
    messageMainPage = MessageMainPage(driver)
    intentionFilterPage = IntentionFilterPage(driver)
    intentionCommunicationPage = IntentionCommunicationPage(driver)
    homePage = HomePage(driver)
    
    with allure.step("点击主页中的消息tab"):
        homePage.click_message_tab()
        screenshot_path = take_screenshot(driver, test_intention_communication.__name__)
        allure.attach.file(screenshot_path, name="点击消息tab", attachment_type=allure.attachment_type.PNG)
    
    with allure.step("点击消息页面中的互动tab"):
        messageMainPage.click_tab_interact()
        screenshot_path = take_screenshot(driver, test_intention_communication.__name__)
        allure.attach.file(screenshot_path, name="点击互动tab", attachment_type=allure.attachment_type.PNG)
    #断言有意向沟通tab
    assert messageMainPage.is_element_visible(*messageMainPage.INTENTION_COMMUNICATION_TAB), "没有意向沟通tab"

    with allure.step("点击意向沟通tab"):
        messageMainPage.click_tab_intention_communication()
        screenshot_path = take_screenshot(driver, test_intention_communication.__name__)
        allure.attach.file(screenshot_path, name="点击意向沟通tab", attachment_type=allure.attachment_type.PNG)
    
    with allure.step("点击意向沟通列表中的第一个牛人卡片"):
        intentionCommunicationPage.click_intention_communication_item(index=0)
        screenshot_path = take_screenshot(driver, test_intention_communication.__name__)
        allure.attach.file(screenshot_path, name="点击牛人卡片", attachment_type=allure.attachment_type.PNG)
    
    with allure.step("返回意向沟通列表"):
        driver.back()
        screenshot_path = take_screenshot(driver, test_intention_communication.__name__)
        allure.attach.file(screenshot_path, name="返回意向沟通列表", attachment_type=allure.attachment_type.PNG)
        # 验证是否成功返回到意向沟通列表页面
        try:
            assert intentionCommunicationPage.is_element_visible(*intentionCommunicationPage.JOB_SELECT_BUTTON), "未能返回到意向沟通列表页面"
        except AssertionError as e:
            pytest.fail(f"返回意向沟通列表失败: {str(e)}")
    
    with allure.step("点击选择职位按钮"):
        intentionCommunicationPage.click_job_select_button()
        screenshot_path = take_screenshot(driver, test_intention_communication.__name__)
        allure.attach.file(screenshot_path, name="点击选择职位", attachment_type=allure.attachment_type.PNG)
    
    with allure.step("点击职位列表中的第1个职位"):
        intentionCommunicationPage.click_job_list_item(index=0)
        screenshot_path = take_screenshot(driver, test_intention_communication.__name__)
        allure.attach.file(screenshot_path, name="选择职位", attachment_type=allure.attachment_type.PNG)
    
    with allure.step("点击条件筛选按钮"):
        intentionCommunicationPage.click_condition_filter_button()
        screenshot_path = take_screenshot(driver, test_intention_communication.__name__)
        allure.attach.file(screenshot_path, name="点击条件筛选", attachment_type=allure.attachment_type.PNG)
    
    with allure.step("选择求职状态-离职随时到岗"):
        swipe_count = 0
        max_swipes = 10
        while not intentionFilterPage.is_element_visible(*intentionFilterPage.RESIGN_OPTION):
            if swipe_count >= max_swipes:
                pytest.fail("未找到离职-随时到岗选项")
                break
            intentionFilterPage.swipe_up(0.2)
            swipe_count += 1
        intentionFilterPage.select_job_intention_condition("离职-随时到岗")
        screenshot_path = take_screenshot(driver, test_intention_communication.__name__)
        allure.attach.file(screenshot_path, name="选择求职状态", attachment_type=allure.attachment_type.PNG)

    with allure.step("选择院校要求-统招本科"):
        swipe_count = 0
        while not intentionFilterPage.is_element_visible(*intentionFilterPage.UNDERGRADUATE_OPTION):
            if swipe_count >= max_swipes:
                pytest.fail("未找到统招本科选项")
                break
            intentionFilterPage.swipe_up(0.2)
            swipe_count += 1
        intentionFilterPage.select_university("统招本科")
        screenshot_path = take_screenshot(driver, test_intention_communication.__name__)
        allure.attach.file(screenshot_path, name="选择院校要求", attachment_type=allure.attachment_type.PNG)

    with allure.step("选择性别要求-男"):
        swipe_count = 0
        while not intentionFilterPage.is_element_visible(*intentionFilterPage.MALE_OPTION):
            if swipe_count >= max_swipes:
                pytest.fail("未找到性别选项")
                break
            intentionFilterPage.swipe_up(0.2)
            swipe_count += 1
        intentionFilterPage.select_gender("男")
        screenshot_path = take_screenshot(driver, test_intention_communication.__name__)
        allure.attach.file(screenshot_path, name="选择性别要求", attachment_type=allure.attachment_type.PNG)

    with allure.step("选择跳槽频率-5年少于3份"):
        swipe_count = 0
        while not intentionFilterPage.is_element_visible(*intentionFilterPage.LESS_THAN_THREE_OPTION):
            if swipe_count >= max_swipes:
                pytest.fail("未找到跳槽频率选项")
                break
            intentionFilterPage.swipe_up(0.2)
            swipe_count += 1
        intentionFilterPage.select_resign_frequency("5年少于3份")
        screenshot_path = take_screenshot(driver, test_intention_communication.__name__)
        allure.attach.file(screenshot_path, name="选择跳槽频率", attachment_type=allure.attachment_type.PNG)
    
    with allure.step("点击确定按钮"):
        intentionFilterPage.click_confirm()
        screenshot_path = take_screenshot(driver, test_intention_communication.__name__)
        allure.attach.file(screenshot_path, name="确认筛选条件", attachment_type=allure.attachment_type.PNG)
    #断言列表中牛人卡片数量
    assert intentionCommunicationPage.get_intention_communication_item_count() >0, "没有召回牛人"
    with allure.step("点击AI帮搜按钮"):
        intentionCommunicationPage.click_ai_help_search_button()
        screenshot_path = take_screenshot(driver, test_intention_communication.__name__)
        allure.attach.file(screenshot_path, name="点击AI帮搜", attachment_type=allure.attachment_type.PNG)
    
    with allure.step("在搜索框中输入'3年经验'"):
        intentionCommunicationPage.click_search_button()
        intentionCommunicationPage.input_search("3年经验")
        screenshot_path = take_screenshot(driver, test_intention_communication.__name__)
        allure.attach.file(screenshot_path, name="输入搜索条件", attachment_type=allure.attachment_type.PNG)