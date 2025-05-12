#推荐牛人列表点击筛选后进入筛选条件选择页面
from pages.base_page import BasePage

class RecommendFilterPage(BasePage):
    """
    推荐牛人列表筛选条件选择页面页面对象
    """
    
    # ========== 顶部导航栏 ==========
    # 返回按钮，点击返回上一页
    BACK_BUTTON = ("id", "com.hpbr.bosszhipin:id/iv_back")
    # 页面标题文本
    TITLE_TEXT = ("id", "com.hpbr.bosszhipin:id/tv_title")
    
    # ========== VIP可用的选项区域 ==========
    # VIP图标
    VIP_ICON = ("id", "com.hpbr.bosszhipin:id/vip_iv")
    # VIP提示文本
    VIP_TIP_TEXT = ("id", "com.hpbr.bosszhipin:id/tv_vip_tip")
    
    # ========== 年龄选择区 ==========
    # 年龄标签
    AGE_LABEL = ("id", "com.hpbr.bosszhipin:id/tv_label")
    # 年龄区间选择器，无法直接操作
    AGE_RANGE_BAR = ("id", "com.hpbr.bosszhipin:id/ZPUIRangeBar")
    
    # ========== 活跃度选择区 ==========
    # 活跃度标签
    ACTIVITY_LABEL = ("xpath", "//android.widget.TextView[@text='活跃度']")
    # 活跃度提示文本（单选）
    ACTIVITY_TIPS = ("id", "com.hpbr.bosszhipin:id/tv_tips")
    # 活跃度选项列表容器
    ACTIVITY_OPTIONS_LIST = ("id", "com.hpbr.bosszhipin:id/rv_keywords")
    # 刚刚活跃选项
    JUST_ACTIVE_OPTION = ("xpath", "//android.widget.TextView[@text=刚刚活跃']")
    # 今日活跃选项
    TODAY_ACTIVE_OPTION = ("xpath", "//android.widget.TextView[@text='今日活跃']")
    # 3日内活跃选项
    THREE_DAY_ACTIVE_OPTION = ("xpath", "//android.widget.TextView[@text='3日内活跃']")
    # 本周活跃选项
    WEEK_ACTIVE_OPTION = ("xpath", "//android.widget.TextView[@text='本周活跃']")
    # 本月活跃选项
    MONTH_ACTIVE_OPTION = ("xpath", "//android.widget.TextView[@text='本月活跃']")
    
    # ========== 性别选择区 ==========
    # 性别标签
    GENDER_LABEL = ("xpath", "//android.widget.TextView[@text='性别']")
    # 不限选项
    ANY_GENDER_OPTION = ("xpath", "//android.widget.TextView[@text='男']/parent::*/preceding-sibling::*[1]")
    # 男选项
    MALE_OPTION = ("xpath", "//android.widget.TextView[@text='男']")
    # 女选项
    FEMALE_OPTION = ("xpath", "//android.widget.TextView[@text='女']")
    
    # ========== 展开更多区 ==========
    # 展开更多按钮
    EXPAND_MORE_BUTTON = ("id", "com.hpbr.bosszhipin:id/filter_vip_expand_layout")
    # 展开更多文本
    EXPAND_MORE_TEXT = ("id", "com.hpbr.bosszhipin:id/tv_content")
    
    # ========== 学历要求选择区 ==========
    # 学历要求标签
    EDUCATION_LABEL = ("xpath", "//android.widget.TextView[@text='学历要求']")
    # 学历要求选项列表容器
    EDUCATION_OPTIONS_LIST = ("id", "com.hpbr.bosszhipin:id/rv_keywords")
    # 全部选项
    ALL_EDUCATION_OPTION = ("xpath", "//android.widget.TextView[@text='初中及以下']/parent::*/preceding-sibling::*[1]")
    # 初中及以下选项
    MIDDLE_SCHOOL_OPTION = ("xpath", "//android.widget.TextView[@text='初中及以下']")
    # 中专/技校选项
    TECHNICAL_SCHOOL_OPTION = ("xpath", "//android.widget.TextView[@text='中专/技校']")
    # 高中选项
    HIGH_SCHOOL_OPTION = ("xpath", "//android.widget.TextView[@text='高中']")
    # 大专选项
    COLLEGE_OPTION = ("xpath", "//android.widget.TextView[@text='大专']")
    # 本科选项
    BACHELORS_OPTION = ("xpath", "//android.widget.TextView[@text='本科']")
    # 硕士选项
    MASTERS_OPTION = ("xpath", "//android.widget.TextView[@text='硕士']")
    # 博士选项
    PHD_OPTION = ("xpath", "//android.widget.TextView[@text='博士']")

    # ========== 经验要求区 ==========
    # 全部选项
    ALL_EXPERIENCE_OPTION = ("xpath", "//android.widget.TextView[@text='在校/应届']/parent::*/preceding-sibling::*[1]")
    # 在校/应届选项
    GRADUATE_OPTION = ("xpath", "//android.widget.TextView[@text='在校/应届']")
    # 1年以内选项
    ONE_YEAR_OPTION = ("xpath", "//android.widget.TextView[@text='1年以内']")
    # 1-3年选项
    ONE_TO_THREE_YEARS_OPTION = ("xpath", "//android.widget.TextView[@text='1-3年']")
    # 3-5年选项
    THREE_TO_FIVE_YEARS_OPTION = ("xpath", "//android.widget.TextView[@text='3-5年']")
    # 5-10年选项
    FIVE_TO_TEN_YEARS_OPTION = ("xpath", "//android.widget.TextView[@text='5-10年']")
    # 10年以上选项
    MORE_THAN_TEN_YEARS_OPTION = ("xpath", "//android.widget.TextView[@text='10年以上']")

    # ========== 求职意向区 ==========
    # 全部选项
    ALL_JOB_INTENTION_OPTION = ("xpath", "//android.widget.TextView[@text='离职-随时到岗']/parent::*/preceding-sibling::*[1]")
    # 离职-随时到岗选项
    RESIGN_OPTION = ("xpath", "//android.widget.TextView[@text='离职-随时到岗']")
    # 在职-考虑机会选项
    CONSIDER_OPPORTUNITY_OPTION = ("xpath", "//android.widget.TextView[@text='在职-考虑机会']")
    # 在职-暂不考虑选项
    NOT_CONSIDER_OPTION = ("xpath", "//android.widget.TextView[@text='在职-暂不考虑']")
    # 在职-月内到岗选项
    MONTH_OPTION = ("xpath", "//android.widget.TextView[@text='月内到岗']")

    # ========== 薪资待遇区 ==========
    # 全部选项
    ALL_SALARY_OPTION = ("xpath", "//android.widget.TextView[@text='3K以下']/parent::*/preceding-sibling::*[1]")
    #3K以下
    LESS_THAN_THREE_THOUSAND_OPTION = ("xpath", "//android.widget.TextView[@text='3K以下']")
    #3-5K
    THREE_TO_FIVE_THOUSAND_OPTION = ("xpath", "//android.widget.TextView[@text='3-5K']")
    #5-10K
    FIVE_TO_TEN_THOUSAND_OPTION = ("xpath", "//android.widget.TextView[@text='5-10K']")
    #10-20K
    TEN_TO_TWENTY_THOUSAND_OPTION = ("xpath", "//android.widget.TextView[@text='10-20K']")
    #20-50K
    TWENTY_TO_FFFY_THOUSAND_OPTION = ("xpath", "//android.widget.TextView[@text='20-55K']")
    #50K以上
    MORE_THAN_FIFTY_THOUSAND_OPTION = ("xpath", "//android.widget.TextView[@text='50K以上']")


    # ========== 底部按钮区 ==========
    # 清除按钮
    RESET_BUTTON = ("id", "com.hpbr.bosszhipin:id/btn_reset")
    # 确定按钮
    CONFIRM_BUTTON = ("id", "com.hpbr.bosszhipin:id/btn_confirm")

    def click_back(self):
        """点击返回按钮"""
        self.find_element(*self.BACK_BUTTON).click()

    def get_title_text(self):
        """获取页面标题文本"""
        return self.find_element(*self.TITLE_TEXT).text

    def is_vip_tip_displayed(self):
        """判断VIP提示是否显示"""
        return self.find_element(*self.VIP_TIP_TEXT).is_displayed()
    
    def get_vip_tip_text(self):
        """获取VIP提示文本内容"""
        return self.find_element(*self.VIP_TIP_TEXT).text

    def adjust_age_range(self, start_percent, end_percent):
        """
        调整年龄区间滑块
        :param start_percent: 开始位置百分比，范围0-100
        :param end_percent: 结束位置百分比，范围0-100
        """
        range_bar = self.find_element(self.AGE_RANGE_BAR)
        # 获取滑块的位置和大小
        bar_location = range_bar.location
        bar_size = range_bar.size
        
        # 计算滑动位置
        start_x = bar_location['x'] + int(bar_size['width'] * start_percent / 100)
        end_x = bar_location['x'] + int(bar_size['width'] * end_percent / 100)
        y = bar_location['y'] + bar_size['height'] // 2
        
        # 模拟滑动操作
        self.driver.tap([(start_x, y)], 500)
        self.driver.tap([(end_x, y)], 500)

    def select_activity_option(self, option_text):
        """
        选择活跃度选项
        :param option_text: 选项文本，如"全部"、"刚刚活跃"等
        """
        option_locator = ("xpath", f"//android.widget.TextView[@text='{option_text}']")
        self.find_element(*option_locator).click()

    def select_gender_option(self, option_text):
        """
        选择性别选项
        :param option_text: 选项文本，如"不限"、"男"、"女"
        """
        option_locator = ("xpath", f"//android.widget.TextView[@text='{option_text}']")
        self.find_element(*option_locator).click()

    def select_job_intention_option(self, option_text):
        """
        选择求职意向选项
        :param option_text: 选项文本，如"全职"、"兼职"等
        """
        option_locator = ("xpath", f"//android.widget.TextView[@text='{option_text}']")
        self.find_element(*option_locator).click()
    
    def select_salary_option(self, option_text):
        """
        选择薪资待遇选项
        :param option_text: 选项文本，如"3K以下"、"3-5K"等
        """
        option_locator = ("xpath", f"//android.widget.TextView[@text='{option_text}']")
        self.find_element(*option_locator).click()

    def click_expand_more(self):
        """点击展开更多选项按钮"""
        self.find_element(self.EXPAND_MORE_BUTTON).click()

    def select_education_option(self, option_text):
        """
        选择学历要求选项
        :param option_text: 选项文本，如"全部"、"本科"等
        """
        option_locator = ("xpath", f"//android.widget.TextView[@text='{option_text}']")
        self.find_element(*option_locator).click()

    def click_reset(self):
        """点击清除按钮"""
        self.find_element(*self.RESET_BUTTON).click()

    def click_confirm(self):
        """点击确定按钮"""
        self.find_element(*self.CONFIRM_BUTTON).click()

    

    def swipe_up(self, percent=0.2):
        """
        向上滑动屏幕
        :param percent: 滑动距离占屏幕高度的百分比
        """
        screen_height = self.driver.get_window_size()['height']
        swipe_distance = int(screen_height * percent)
        #滑动起点不能是最顶部和最底部,终点为根据百分比计算
        start_y = screen_height * 0.8
        self.driver.swipe(0, start_y, 0, swipe_distance, duration=500)
    