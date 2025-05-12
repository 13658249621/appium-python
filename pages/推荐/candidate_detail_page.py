from pages.base_page import BasePage


class CandidateDetailPage(BasePage):
    """
    推荐牛人详情页页面对象
    """

    # ===== 顶部导航栏 =====
    # 返回按钮
    BACK_BUTTON = ('id', 'com.hpbr.bosszhipin:id/iv_back')
    # 顶部操作按钮区，数量可能动态变化，一般情况下有收藏、分享、和更多按钮
    TITLE_ACTIONS = ('id', 'com.hpbr.bosszhipin:id/title_actions')

    # ===== 候选人信息卡片 =====
    # 头像
    AVATAR = ('id', 'com.hpbr.bosszhipin:id/iv_avatar')
    # 姓名
    NAME = ('id', 'com.hpbr.bosszhipin:id/tv_geek_name')
    # 性别图标
    GENDER_ICON = ('id', 'com.hpbr.bosszhipin:id/iv_gender')
    # 职位公司
    JOB_AND_COMPANY = ('id', 'com.hpbr.bosszhipin:id/tv_job_and_com')
    # 求职状态
    WORK_STATUS = ('id', 'com.hpbr.bosszhipin:id/tv_geek_work_status')
    # 在线状态
    ONLINE_STATE_ICON = ('id', 'com.hpbr.bosszhipin:id/iv_online_state')
    # 工作年限
    WORK_YEAR = ('id', 'com.hpbr.bosszhipin:id/tv_geek_work_year')
    # 学历
    DEGREE = ('id', 'com.hpbr.bosszhipin:id/tv_geek_degree')
    # 年龄
    AGE = ('id', 'com.hpbr.bosszhipin:id/tv_geek_age')
    # 个人优势/自我介绍
    DESCRIPTION = ('id', 'com.hpbr.bosszhipin:id/tv_geek_description')
    # 技能标签（可能有多个）
    SKILL_TAG = ('id', 'com.hpbr.bosszhipin:id/txt_content')

    # ===== 简历获取 =====
    # 牛人简历上传状态标题
    RESUME_TITLE = ('id', 'com.hpbr.bosszhipin:id/tv_title')
    # 简历获取按钮
    RESUME_BUTTON = ('id', 'com.hpbr.bosszhipin:id/btn_desc')

    # ===== 求职期望模块 =====
    # 期望职位名称和城市
    EXPECTED_JOB_AND_CITY = ('id', 'com.hpbr.bosszhipin:id/tv_job_and_city')
    # 期望薪资
    EXPECTED_SALARY = ('id', 'com.hpbr.bosszhipin:id/tv_salary')

    # ===== 工作经历模块 =====
    # 工作经历公司信息
    WORK_COMPANY = ('id', 'com.hpbr.bosszhipin:id/tv_work_company')
    # 工作经历工作时间
    TIME_RANGE = ('id', 'com.hpbr.bosszhipin:id/tv_time_range')
    # 工作经历职位名称
    JOB_NAME = ('id', 'com.hpbr.bosszhipin:id/tv_job_name')


    # ===== 分区标题/分割线 =====
    SECTION_TITLE = ('id', 'com.hpbr.bosszhipin:id/tv_section_title')
    DIVIDER = ('id', 'com.hpbr.bosszhipin:id/view_divider')

    # ===== 底部操作栏 =====    
    # 底部操作栏，可能动态变化，一般情况下有立即沟通、继续沟通、不合适按钮。只有一个按钮时可能为立即沟通或继续沟通，有两个按钮时可能为不合适和继续沟通
    BOTTOM_ACTIONS = ('id', 'com.hpbr.bosszhipin:id/bottom_buttons_layout')
    # 立即沟通按钮,点击之后会变为继续沟通
    COMMUNICATE_BUTTON = ('xpath', '//android.widget.Button[@text="立即沟通"]')
    # 继续沟通按钮
    CONTINUE_COMMUNICATE_BUTTON = ('xpath', '//android.widget.Button[@text="继续沟通"]')
    # 已经开聊的牛人退出详情页后，再次进入，继续沟通会变为不合适和继续沟通
    # 不合适按钮
    INAPPROPRIATE_BUTTON = ('xpath', '//android.widget.Button[@text="不合适"]')

    # ========== 操作方法 ==========

    # ===== 顶部导航栏 =====
    # 点击返回按钮
    def click_back_button(self):
        """点击页面左上角返回按钮"""
        self.click(*self.BACK_BUTTON)

    # ===== 候选人信息 =====
    # 获取候选人姓名
    def get_candidate_name(self):
        """获取候选人姓名文本"""
        return self.find_element(*self.NAME).text

    # 获取候选人头像元素
    def get_avatar_element(self):
        """获取候选人头像元素对象"""
        return self.find_element(*self.AVATAR)
    #求职状态
    def get_work_status(self):
        """获取求职状态文本"""
        return self.find_element(*self.WORK_STATUS).text
    #学历
    def get_degree(self):
        """获取学历文本"""
        return self.find_element(*self.DEGREE).text
    #工作年限
    def get_work_year(self):
        """获取工作年限文本"""
        return self.find_element(*self.WORK_YEAR).text
    #年龄
    def get_age(self):
        """获取年龄文本"""
        return self.find_element(*self.AGE).text
    # 获取个人优势/自我介绍
    def get_description(self):
        """获取技能描述文本"""
        return self.find_element(*self.DESCRIPTION).text

    # 获取技能标签文本列表
    def get_skill_tags(self):
        """获取所有技能标签文本列表"""
        tags = self.find_elements(*self.SKILL_TAG)
        return [tag.text for tag in tags] if tags else []

    # ===== 简历获取 =====
    # 点击简历获取按钮
    def click_resume_button(self):
        """点击简历上传区的沟通获取按钮"""
        self.click(*self.RESUME_BUTTON)

    # ===== 求职期望模块 =====
    # 获取期望职位名称
    def get_expected_job(self):
        """获取期望职位名称"""
        text = self.find_element(*self.EXPECTED_JOB_AND_CITY).text
        return text.split('·')[0].strip()

    # 获取期望城市
    def get_expected_city(self):
        """获取期望城市"""
        text = self.find_element(*self.EXPECTED_JOB_AND_CITY).text
        return text.split('·')[1].strip()

    # 获取期望薪资
    def get_expected_salary(self):
        """获取期望薪资"""
        return self.find_element(*self.EXPECTED_SALARY).text

    # ===== 工作经历模块 =====
    # 获取公司信息
    def get_work_company(self):
        """获取公司信息文本"""
        return self.find_element(*self.WORK_COMPANY).text

    # ===== 工作经历模块 =====
    # 获取担任职位名称
    def get_job_name(self):
        """获取职位名称文本"""
        return self.find_element(*self.JOB_NAME).text


    # 点击立即沟通
    def click_communicate_button(self):
        """点击底部立即沟通按钮"""
        self.click(*self.COMMUNICATE_BUTTON)
