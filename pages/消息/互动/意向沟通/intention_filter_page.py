from pages.base_page import BasePage

class IntentionFilterPage(BasePage):
    """
    意向沟通-筛选页面
    """
    
    # 返回按钮
    BACK_BUTTON = ('id', 'com.hpbr.bosszhipin:id/iv_back')
    

    # 学历要求
    DEGREE_RANGE = ('id', 'com.hpbr.bosszhipin:id/range_degree')
    # 工作经验
    WORK_YEAR_TEXT = ('id', 'com.hpbr.bosszhipin:id/tv_work_year')
    WORK_YEAR_RANGE = ('id', 'com.hpbr.bosszhipin:id/range_work_year')
    # 期望薪资
    WORK_SALARY_TEXT = ('id', 'com.hpbr.bosszhipin:id/tv_work_salary')
    WORK_SALARY_RANGE = ('id', 'com.hpbr.bosszhipin:id/range_work_salary')

    # ========== 求职状态 ==========
    CONDITION_TITLE_TEXT = ('id', 'com.hpbr.bosszhipin:id/tv_condition_title')
    CONDITION_KEYWORDS = ('xpath', '//android.widget.TextView[@resource-id="com.hpbr.bosszhipin:id/keywords_view_text"]')
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

    # ========== 年龄要求 ==========
    AGE_TEXT = ('id', 'com.hpbr.bosszhipin:id/tv_age')
    AGE_RANGE = ('id', 'com.hpbr.bosszhipin:id/range_age')

    # ========== 院校要求 ==========
    # 全部选项
    ALL_UNIVERSITY_OPTION = ("xpath", "//android.widget.TextView[@text='统招本科']/parent::*/preceding-sibling::*[1]")
    # 统招本科
    UNDERGRADUATE_OPTION = ("xpath", "//android.widget.TextView[@text='统招本科']")
    #双一流院校
    DOUBLE_FIRST_CLASS_OPTION = ("xpath", "//android.widget.TextView[@text='双一流院校']")
    # 985院校
    NINTEEN_EIGHT_FIVE_OPTION = ("xpath", "//android.widget.TextView[@text='985院校']")
    # 211院校
    TWENTY_ONE_ONE_OPTION = ("xpath", "//android.widget.TextView[@text='211院校']")
    # 留学生
    OVERSEAS_STUDENT_OPTION = ("xpath", "//android.widget.TextView[@text='留学生']")

    # ========== 性别要求 ==========
    # 全部选项
    ALL_GENDER_OPTION = ("xpath", "//android.widget.TextView[@text='男']/parent::*/preceding-sibling::*[1]")
    # 男
    MALE_OPTION = ("xpath", "//android.widget.TextView[@text='男']")
    # 女
    FEMALE_OPTION = ("xpath", "//android.widget.TextView[@text='女']")

    # ========== 跳槽频率 ==========
    # 全部选项
    ALL_RESIGN_FREQUENCY_OPTION = ("xpath", "//android.widget.TextView[@text='5年少于3份']/parent::*/preceding-sibling::*[1]")
    # 5年少于3份
    LESS_THAN_THREE_OPTION = ("xpath", "//android.widget.TextView[@text='5年少于3份']")
    # 时间≥1年
    ONE_YEAR_OPTION = ("xpath", "//android.widget.TextView[@text='时间≥1年']")

    # 清除按钮
    RESET_BUTTON = ('id', 'com.hpbr.bosszhipin:id/btn_reset')
    # 确定按钮
    CONFIRM_BUTTON = ('id', 'com.hpbr.bosszhipin:id/btn_confirm')


    def get_work_year_text(self):
        """获取工作经验文本"""
        return self.get_text(*self.WORK_YEAR_TEXT)

    def get_work_salary_text(self):
        """获取期望薪资文本"""
        return self.get_text(*self.WORK_SALARY_TEXT)

    def get_condition_title_text(self):
        """获取求职状态标题文本"""
        return self.get_text(*self.CONDITION_TITLE_TEXT)

    def get_age_text(self):
        """获取年龄要求文本"""
        return self.get_text(*self.AGE_TEXT)
    # ========== 求职状态 ==========
    def select_job_intention_condition(self, text):
        """选择求职状态"""
        if text == "离职-随时到岗":
            self.click(*self.RESIGN_OPTION)
        elif text == "在职-考虑机会":
            self.click(*self.CONSIDER_OPPORTUNITY_OPTION)
        elif text == "在职-暂不考虑":
            self.click(*self.NOT_CONSIDER_OPTION)
        elif text == "月内到岗":
            self.click(*self.MONTH_OPTION)
        elif text == "不限":
            self.click(*self.ALL_JOB_INTENTION_OPTION)

    # ========== 院校要求 ==========
    def select_university(self, text):
        """选择院校"""
        if text == "统招本科":
            self.click(*self.UNDERGRADUATE_OPTION)
        elif text == "双一流院校":
            self.click(*self.DOUBLE_FIRST_CLASS_OPTION)
        elif text == "985院校":
            self.click(*self.NINTEEN_EIGHT_FIVE_OPTION)
        elif text == "211院校":
            self.click(*self.TWENTY_ONE_ONE_OPTION)
        elif text == "留学生":
            self.click(*self.OVERSEAS_STUDENT_OPTION)
        elif text == "不限":
            self.click(*self.ALL_UNIVERSITY_OPTION)
    # ========== 性别要求 ==========
    def select_gender(self, text):
        """选择性别"""
        if text == "男":
            self.click(*self.MALE_OPTION)
        elif text == "女":
            self.click(*self.FEMALE_OPTION)
        elif text == "不限":
            self.click(*self.ALL_GENDER_OPTION)

    # ========== 跳槽频率 ==========
    def select_resign_frequency(self, text):
        """选择跳槽频率"""
        if text == "5年少于3份":
            self.click(*self.LESS_THAN_THREE_OPTION)
        elif text == "时间≥1年":
            self.click(*self.ONE_YEAR_OPTION)
        elif text == "不限":
            self.click(*self.ALL_RESIGN_FREQUENCY_OPTION)

    def click_back(self):
        """点击返回按钮"""
        self.click(*self.BACK_BUTTON)

    def click_reset(self):
        """点击清除按钮"""
        self.click(*self.RESET_BUTTON)

    def click_confirm(self):
        """点击确定按钮"""
        self.click(*self.CONFIRM_BUTTON)

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