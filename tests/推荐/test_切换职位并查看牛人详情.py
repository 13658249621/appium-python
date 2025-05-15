from time import sleep

import allure
from pages.推荐.recommend_main_page import RecommendMainPage
from pages.推荐.candidate_detail_page import CandidateDetailPage
from utils.screenshot_utils import take_screenshot
import pytest
from utils.logger import get_logger
logger = get_logger()

def test_切换职位并查看牛人详情(driver):
    recommend_main_page = RecommendMainPage(driver)
    screenshot_path = take_screenshot(driver, test_切换职位并查看牛人详情.__name__)
    with allure.step("主页"):
        allure.attach.file(screenshot_path, name="主页", attachment_type=allure.attachment_type.PNG)
    #如果职位数量大于1，点击切换到第二个职位
    job_count = recommend_main_page.get_job_count()
    if len(job_count) > 1:
        recommend_main_page.switch_job_tab(2)
    screenshot_path = take_screenshot(driver, test_切换职位并查看牛人详情.__name__)
    with allure.step("切换职位"):
        allure.attach.file(screenshot_path, name="切换职位", attachment_type=allure.attachment_type.PNG)
    #判断候选人列表是否返回了数据
    candidate_count = recommend_main_page.get_candidate_count()
    assert candidate_count > 0, "候选人卡片数量不足,无法点击"
    #获取第一个候选人卡片信息
    candidate_info = recommend_main_page.get_candidate_info(0)
    logger.info(f"候选人列表中第一个候选人的信息: {candidate_info}")
    #点击第一个候选人卡片
    recommend_main_page.click_candidate(0)
    sleep(1)
    screenshot_path = take_screenshot(driver, test_切换职位并查看牛人详情.__name__)
    with allure.step("查看牛人详情"):
        allure.attach.file(screenshot_path, name="查看牛人详情", attachment_type=allure.attachment_type.PNG)
    #进入详情页，获取详情页信息
    detail_page = CandidateDetailPage(driver)
    detail_name = detail_page.get_candidate_name()
    detail_salary = detail_page.get_expected_salary()
    detail_degree = detail_page.get_degree()
    logger.info(f"详情页牛人信息: 姓名={detail_name}, 期望薪资={detail_salary}, 学历={detail_degree}")
    # 断言详情页信息与卡片信息一致
    with allure.step("断言详情页与列表卡片信息一致"):
        # 断言姓名一致
        assert detail_name == candidate_info["name"], \
            f"详情页姓名({detail_name})与卡片姓名({candidate_info['name']})不一致"
        
        # 断言学历一致
        assert detail_degree == candidate_info["degree"], \
            f"详情页学历({detail_degree})与卡片学历({candidate_info['degree']})不一致"
            
        # 断言期望薪资一致
        assert detail_salary == candidate_info["salary"], \
            f"详情页期望薪资({detail_salary})与卡片期望薪资({candidate_info['salary']})不一致"

    # 断言后截图
    screenshot_path = take_screenshot(driver, test_切换职位并查看牛人详情.__name__)
    with allure.step("断言后截图"):
        allure.attach.file(screenshot_path, name="断言后截图", attachment_type=allure.attachment_type.PNG)
