from time import sleep

import allure
from pages.推荐.recommend_main_page import RecommendMainPage
from pages.推荐.candidate_detail_page import CandidateDetailPage
from utils.screenshot_utils import take_screenshot
import pytest
from utils.logger import get_logger
from pages.推荐.recommend_filter_page import RecommendFilterPage

logger = get_logger()

def test(driver):
    recommend_main_page = RecommendMainPage(driver)
    filter_page = RecommendFilterPage(driver)

    # 1. 排序方式切换
    recommend_main_page.select_sort_type("最新")
    sleep(2)
    candidate_count = recommend_main_page.get_candidate_count()
    assert candidate_count > 0

    recommend_main_page.select_sort_type("推荐")
    sleep(2)
    candidate_count = recommend_main_page.get_candidate_count()
    assert candidate_count > 0
    screenshot_path = take_screenshot(driver, test.__name__)
    with allure.step("排序后截图"):
        allure.attach.file(screenshot_path, name="排序后截图", attachment_type=allure.attachment_type.PNG)

    # 2. 城市选择
    recommend_main_page.click_city_button()
    # 返回上一页
    driver.back()

    # 3. 筛选条件选择
    recommend_main_page.click_filter()
    # 学历选择
    max_swipes = 5  # 最大滑动次数
    swipe_count = 0
    while not filter_page.is_element_visible(*filter_page.BACHELORS_OPTION):
        if swipe_count >= max_swipes:
            pytest.fail("未找到本科选项")
            break
        filter_page.swipe_up(0.2)
        swipe_count += 1
    filter_page.select_education_option("本科")
    
    # 求职意向选择
    swipe_count = 0
    while not filter_page.is_element_visible(*filter_page.ALL_JOB_INTENTION_OPTION):
        if swipe_count >= max_swipes:
            pytest.fail("未找到求职意向选项")
            break
        filter_page.swipe_up(0.2)
        swipe_count += 1
    filter_page.select_job_intention_option("离职-随时到岗")
    screenshot_path = take_screenshot(driver, test.__name__)
    with allure.step("筛选后截图"):
        allure.attach.file(screenshot_path, name="筛选后截图", attachment_type=allure.attachment_type.PNG)    

    # 薪资待遇选择
    swipe_count = 0
    while not filter_page.is_element_visible(*filter_page.ALL_SALARY_OPTION):
        if swipe_count >= max_swipes:
            pytest.fail("未找到薪资待遇选项")
            break
        filter_page.swipe_up(0.2)
        swipe_count += 1
    filter_page.select_salary_option("10-20K")
    screenshot_path = take_screenshot(driver, test.__name__)
    with allure.step("筛选后截图1"):
        allure.attach.file(screenshot_path, name="筛选后截图1", attachment_type=allure.attachment_type.PNG)

    filter_page.click_confirm()
    sleep(2)
    screenshot_path = take_screenshot(driver, test.__name__)
    with allure.step("确认后截图"):
        allure.attach.file(screenshot_path, name="确认后截图", attachment_type=allure.attachment_type.PNG)
    
    #断言列表中牛人卡片数量
    assert recommend_main_page.get_candidate_count() > 0, "没有召回牛人"

    #获取候选人列表所有卡片，验证卡片上展示学历与筛选条件中选择的学历一致
    candidate_info_list = recommend_main_page.get_all_candidate_info()
    for info in candidate_info_list:
        assert info["degree"] == '本科'
    
    #进入候选人详情页，验证候选人详情页上展示的求职状态与筛选条件中选择的求职状态一致
    recommend_main_page.click_candidate(0)
    candidate_detail_page = CandidateDetailPage(driver)
    assert candidate_detail_page.get_work_status() == '离职-随时到岗'
    screenshot_path = take_screenshot(driver, test.__name__)
    with allure.step("候选人详情页截图"):
        allure.attach.file(screenshot_path, name="候选人详情页截图", attachment_type=allure.attachment_type.PNG)    


