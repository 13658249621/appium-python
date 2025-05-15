# -*- coding: utf-8 -*-
"""
CandidateDetailPage 页面对象

封装了意向沟通牛人详情页的主要操作，包括发起意向、职位选择等。
"""
from pages.base_page import BasePage

class CandidateDetailPage(BasePage):
    #==============意向沟通牛人详情页=============
    #帮我问意向按钮
    ASK_INTENTION_BUTTON = ('id', 'com.hpbr.bosszhipin:id/bottom_buttons_layout')

    #==============发起问意向弹层=============
    # 关闭问意向弹层按钮
    CLOSE_BUTTON = ('id', 'com.hpbr.bosszhipin:id/mCloseView')
    # 职位选择按钮,具有text属性:机电工程师 · 6-10K · 北京
    POSITION_BUTTON = ('id', 'com.hpbr.bosszhipin:id/mPositionView')
    # 反馈时间提示文案：(2个工作日内反馈)
    FEEDBACK_HINT_TEXT = ('id', 'com.hpbr.bosszhipin:id/mFeedBackMsgView')


    #==============职位选择弹层=============
    #职位选择弹层的标题
    POSITION_SELECT_TITLE = ('xpath', '//android.widget.TextView[@text="选择职位"]')
    #职位选择弹层返回按钮
    POSITION_SELECT_BACK_BUTTON = ('id', 'com.hpbr.bosszhipin:id/mBackView')
    #职位列表容器
    POSITION_LIST_CONTAINER = ('id', 'com.hpbr.bosszhipin:id/mContainer')
    #职位列表所有职位选项
    POSITION_LIST_ITEMS = ('xpath', '//android.widget.LinearLayout[@resource-id="com.hpbr.bosszhipin:id/mContainer"]/android.widget.LinearLayout')
    #职位列表项所有职位名称*薪资：机电工程师 · 6-10K
    POSITION_NAME = ('xpath', '//android.widget.LinearLayout[@resource-id="com.hpbr.bosszhipin:id/mContainer"]/android.widget.LinearLayout/android.widget.TextView[1]')

    #==============添加注意事模块==============
    # 添加注意事模块
    ADD_WARNING_DETAIL = ('id', 'com.hpbr.bosszhipin:id/mAddWarningDetail')
    # 注意事项选择项容器
    WARNING_SELECT_CONTAINER = ('id', 'com.hpbr.bosszhipin:id/mWaringEventContainer')
    # ==========注意事项选择项和输入框==========
    #所有注意事项选择项
    WARNING_OPTIONS = ('xpath', '//android.widget.TextView[@resource-id="com.hpbr.bosszhipin:id/mTextView"]')
    # 薪资职级可适当调整
    SALARY_LEVEL_ADJUSTABLE = ('xpath', '//android.widget.TextView[@resource-id="com.hpbr.bosszhipin:id/mTextView" and @text="薪资职级可适当调整"]')
    # 其他城市有办公点
    OTHER_CITY_HAS_OFFICE = ('xpath', '//android.widget.TextView[@resource-id="com.hpbr.bosszhipin:id/mTextView" and @text="其他城市有办公点"]')
    # 接受兼职/线上办公
    ACCEPT_PART_TIME_OR_ONLINE_OFFICE = ('xpath', '//android.widget.TextView[@resource-id="com.hpbr.bosszhipin:id/mTextView" and @text="接受兼职/线上办公"]')
    # 注意事项输入框
    WARNING_INPUT = ('id', 'com.hpbr.bosszhipin:id/mEditTextView')
    # 输入字数统计,有text属性:2/100
    INPUT_TEXT_COUNT = ('id', 'com.hpbr.bosszhipin:id/mInputTextCount')

    # 权益说明文案，畅聊版权益:发起沟通消耗1次权益，打不通补偿权益
    NOTICE_TEXT = ('id', 'com.hpbr.bosszhipin:id/mNoticeText')


    # "请TA沟通"按钮/确认发起问意向按钮
    CONTACT_BUTTON = ('id', 'com.hpbr.bosszhipin:id/mContactView')



    def click_ask_intention_button(self):
        """
        点击帮我问意向按钮
        """
        self.click(*self.ASK_INTENTION_BUTTON)

    def click_close_button(self):
        """
        点击关闭问意向弹层按钮
        """
        self.click(*self.CLOSE_BUTTON)

    def click_position_selector(self):
        """
        点击职位选择按钮
        """
        self.click(*self.POSITION_BUTTON)
    
    def get_position_button_text(self):
        """
        获取职位选择按钮的文本
        """
        return self.find_element(*self.POSITION_BUTTON).text

    def get_position_select_title(self):
        """
        获取职位选择弹层的标题
        """
        return self.find_element(*self.POSITION_SELECT_TITLE).text

    def click_position_select_back_button(self):
        """
        点击职位选择弹层返回按钮
        """
        self.click(*self.POSITION_SELECT_BACK_BUTTON)

    def get_position_list_items(self):
        """
        获取职位列表项
        """
        return self.find_elements(*self.POSITION_LIST_ITEMS)
    
    def select_position(self, index=1):
        """
        选择第x个职位
        """
        elements = self.find_elements(*self.POSITION_LIST_ITEMS)
        if elements:
            elements[index-1].click()
    
    def get_feedback_hint_text(self):
        """
        获取反馈时间提示文本
        :return: str
        """
        element = self.find_element(*self.FEEDBACK_HINT_TEXT)
        return element.text if element else None

    #选择第x个注意事项选项
    def select_warning_option(self, index=1):
        """
        选择意事项选项
        :param index: 选项索引
        """
        elements = self.find_elements(*self.WARNING_OPTIONS)
        if elements:
            elements[index-1].click()


    def input_warning(self, text):
        """
        在注意事项输入框输入内容
        :param text: 输入内容
        """
        self.input(*self.WARNING_INPUT, text)


    def get_input_text_count(self):
        """
        获取输入字数统计
        :return: str
        """
        #2/100需要进行切割 切割后返回2
        element = self.find_element(*self.INPUT_TEXT_COUNT)
        return element.text.split('/') if element else None

    def get_notice_text(self):
        """
        获取权益说明文本
        :return: str
        """
        element = self.find_element(*self.NOTICE_TEXT)
        return element.text if element else None 


    def click_contact_button(self):
        """
        点击"请TA沟通"按钮
        """
        self.click(*self.CONTACT_BUTTON)