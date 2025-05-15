# -*- coding: utf-8 -*-
"""
SearchResultPage 页面对象

封装了Boss直聘App搜索结果页面的主要操作，包括候选人卡片操作、筛选等。
"""
from pages.base_page import BasePage

class SearchResultPage(BasePage):
    #== 搜索结果列表 ==
    # 牛人卡片列表
    CANDIDATE_CARD_LIST = ('xpath', '//android.view.ViewGroup[@resource-id="com.hpbr.bosszhipin:id/cl_search_card"]')
    # 牛人卡片(第一个)
    CANDIDATE_CARD = ('xpath', '(//android.view.ViewGroup[@resource-id="com.hpbr.bosszhipin:id/cl_search_card"])[1]')
    
    #== 排序选择 ==
    # 排序选择按钮
    SORT_FILTER_BUTTON = ('xpath', '//android.widget.TextView[@resource-id="com.hpbr.bosszhipin:id/tv_display_name" and @text="排序"]')
    # 活跃优先选项
    ACTIVE_FIRST_OPTION = ('xpath', '//android.widget.TextView[@resource-id="com.hpbr.bosszhipin:id/tv_content" and @text="活跃优先"]')
    # 学历筛选项
    EDUCATION_FILTER_OPTION = ('xpath', '//android.widget.TextView[@resource-id="com.hpbr.bosszhipin:id/tv_display_name" and @text="学历"]')
    # 离职-随时到岗选项
    AVAILABLE_IMMEDIATELY_OPTION = ('xpath', '//android.widget.TextView[@resource-id="com.hpbr.bosszhipin:id/keywords_view_text" and @text="离职-随时到岗"]')
    # 筛选界面确认按钮
    CONFIRM_BUTTON = ('id', 'com.hpbr.bosszhipin:id/btn_confirm')
    
    def get_candidate_card_count(self):
        """
        获取牛人卡片数量
        :return: int
        """
        cards = self.find_elements(*self.CANDIDATE_CARD)
        return len(cards) if cards else 0

    def click_sort_filter_option(self):
        """
        点击排序筛选项
        :return: None
        """
        self.click(*self.SORT_FILTER_OPTION)

    def click_active_first_option(self):
        """
        选择活跃优先选项
        :return: None
        """
        self.click(*self.ACTIVE_FIRST_OPTION)

    def click_education_filter_option(self):
        """
        点击学历筛选项
        :return: None
        """
        self.click(*self.EDUCATION_FILTER_OPTION)

    def click_available_immediately_option(self):
        """
        选择离职-随时到岗选项
        :return: None
        """
        self.click(*self.AVAILABLE_IMMEDIATELY_OPTION)

    def click_confirm_button(self):
        """
        点击确认按钮
        :return: None
        """
        self.click(*self.CONFIRM_BUTTON) 