# 搜索结果页面
from pages.base_page import BasePage

class SearchResultPage(BasePage):
    # 牛人卡片(第一个)
    CANDIDATE_CARD = ('xpath', '(//android.view.ViewGroup[@resource-id="com.hpbr.bosszhipin:id/cl_search_card"])[1]')
    
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
    
    # 点击第一个牛人卡片
    def click_first_candidate_card(self):
        self.click(*self.CANDIDATE_CARD)
        
    # 点击排序选择按钮
    def click_sort_filter_option(self):
        self.click(*self.SORT_FILTER_BUTTON)
        
    # 点击活跃优先选项
    def click_active_first_option(self):
        self.click(*self.ACTIVE_FIRST_OPTION)
        
    # 点击学历筛选项
    def click_education_filter_option(self):
        self.click(*self.EDUCATION_FILTER_OPTION)
        
    # 点击离职-随时到岗选项
    def click_available_immediately_option(self):
        self.click(*self.AVAILABLE_IMMEDIATELY_OPTION)
        
    # 点击筛选界面确认按钮
    def click_confirm_button(self):
        self.click(*self.CONFIRM_BUTTON) 