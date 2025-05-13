from pages.base_page import BasePage

class IntentionCommunicationPage(BasePage):
    """
    互动-意向沟通页面中的对象
    """
    # 顶部权益提示
    TOP_TIP_ICON = ('id', 'com.hpbr.bosszhipin:id/iv_icon')
    TOP_TIP_TEXT = ('id', 'com.hpbr.bosszhipin:id/tv_tip')
    
    #==================意向沟通候选人列表模块==================
    # 意向沟通候选人列表容器
    CANDIDATE_LIST = ('id', 'com.hpbr.bosszhipin:id/rv_list')
    # 意向沟通候选列表item卡片，一页有多个
    INTENTION_COMMUNICATION_ITEM = (
        'xpath', '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.hpbr.bosszhipin:id/rv_list"]//android.view.ViewGroup[@resource-id="com.hpbr.bosszhipin:id/cl_root"]')
    # 牛人头像
    CANDIDATE_AVATAR = ('id', 'com.hpbr.bosszhipin:id/iv_avatar')
    # 牛人性别icon
    CANDIDATE_GENDER_ICON = ('id', 'com.hpbr.bosszhipin:id/iv_gender')
    # 牛人姓名
    CANDIDATE_NAME = ('id', 'com.hpbr.bosszhipin:id/tv_name')
    # 牛人基本信息
    CANDIDATE_INFO = ('id', 'com.hpbr.bosszhipin:id/tv_info')
    # 牛人工作经历
    CANDIDATE_EXP = ('id', 'com.hpbr.bosszhipin:id/tv_exp')
    # 牛人教育经历
    CANDIDATE_EDU = ('id', 'com.hpbr.bosszhipin:id/tv_edu')
    # 牛人技能标签容器
    CANDIDATE_SKILL_CONTAINER = ('id', 'com.hpbr.bosszhipin:id/fl_layout')
    # 牛人技能标签
    CANDIDATE_SKILL_LABEL = ('xpath', '//android.view.ViewGroup[@resource-id="com.hpbr.bosszhipin:id/fl_layout"]/android.widget.TextView')

    
    #下方职位选择、条件筛选、AI帮搜
    #职位选择按钮
    JOB_SELECT_BUTTON = ('id', 'com.hpbr.bosszhipin:id/fl_filter_position')
    #条件筛选按钮
    CONDITION_FILTER_BUTTON = ('id', 'com.hpbr.bosszhipin:id/fl_filter_condition')
    #AI帮搜按钮
    AI_HELP_SEARCH_BUTTON = ('id', 'com.hpbr.bosszhipin:id/fl_filter_ai_helper')
    
    #==职位选择弹层==
    #职位列表item中的职位名称和薪资拼接文案，可能多个,text：python开发 10-11K
    JOB_LIST_ITEM = ('xpath', '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.hpbr.bosszhipin:id/rv_list"]/android.view.ViewGroup/android.widget.TextView')

    # 搜索输入框
    SEARCH_INPUT = ('xpath', '//android.widget.EditText[@text="试试提出你的要求"]')




    #==顶部权益提示模块==
    def get_top_tip(self):
        """获取顶部权益提示"""
        return self.get_text(*self.TOP_TIP_TEXT)

    def click_msg_item(self, index=0):
        """点击消息列表中的第N个item，默认第一个"""
        items = self.find_elements(*self.MSG_LIST_VIEW)
        if items and len(items) > index:
            items[index].click()

    #==意向沟通候选人列表模块==
    def get_intention_communication_item_count(self):
        """获取意向沟通列表中的牛人卡片数量"""
        items = self.find_elements(*self.INTENTION_COMMUNICATION_ITEM)
        return len(items) if items else 0

    def click_intention_communication_item(self, index=2):
        """点击意向沟通列表中的第N个item，默认第3个（index=2）"""
        items = self.find_elements(*self.INTENTION_COMMUNICATION_ITEM)
        if items and len(items) > index:
            items[index].click()

    #==选择职位、条件筛选、AI帮搜==
    def click_job_select_button(self):
        """点击职位选择按钮"""
        self.click(*self.JOB_SELECT_BUTTON)

    def click_condition_filter_button(self):
        """点击条件筛选按钮"""
        self.click(*self.CONDITION_FILTER_BUTTON)

    def click_ai_help_search_button(self):
        """点击AI帮搜按钮"""
        self.click(*self.AI_HELP_SEARCH_BUTTON)

    #==职位选择弹层==
    def click_job_list_item(self, index=0):
        """点击职位列表中的第N个item，默认第一个"""
        items = self.find_elements(*self.JOB_LIST_ITEM)
        if items and len(items) > index:
            items[index].click()

    #==AI帮搜==
    def click_search_button(self):
        """点击搜索输入框"""
        self.click(*self.SEARCH_INPUT)

    def input_search(self, text):
        """在搜索输入框输入内容"""
        self.input(*self.SEARCH_INPUT, text)