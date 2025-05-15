#意向沟通主页
from pages.base_page import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

# -*- coding: utf-8 -*-
"""
意向沟通主页页面对象
"""
class IntentionCommunicationMainPage(BasePage):
    # 权益明细按钮
    RIGHTS_DETAIL_BUTTON = ('xpath', '//android.widget.TextView[@resource-id="com.hpbr.bosszhipin:id/tv_action"]')
    # 可用按钮
    AVAILABLE_BUTTON = ('xpath', '//android.view.View[contains(@text, "可用")]')
    # 去购买图片按钮
    PURCHASE_BUTTON_IMAGE = './pages/去购买.jpg'
    # 立即购买图片按钮
    BUY_NOW_BUTTON_IMAGE = './pages/立即购买.jpg'

    # ============我的订单页面新增元素============
    # 返回按钮（resource-id="com.hpbr.bosszhipin:id/iv_back"）
    BACK_BUTTON = ('id', 'com.hpbr.bosszhipin:id/iv_back')
    # 我的订单tab（text="我的订单"）
    MY_ORDER_TAB = ('xpath', '//android.widget.TextView[@text="我的订单"]')
    # 意向沟通tab（text="意向沟通"）
    INTENTION_COMMUNICATION_TAB = ('xpath', '//android.widget.TextView[@text="意向沟通"]')
    # 权益明细按钮（resource-id="com.hpbr.bosszhipin:id/tv_action"）
    RIGHTS_DETAIL_BUTTON = ('id', 'com.hpbr.bosszhipin:id/tv_action')
    # 订单列表容器（resource-id="com.hpbr.bosszhipin:id/vp_order"）
    ORDER_LIST_CONTAINER = ('id', 'com.hpbr.bosszhipin:id/vp_order')
    # 订单RecyclerView（resource-id="com.hpbr.bosszhipin:id/rv_list"）
    ORDER_RECYCLER_VIEW = ('id', 'com.hpbr.bosszhipin:id/rv_list')
    # 订单关闭按钮（resource-id="com.hpbr.bosszhipin:id/iv_close"）
    ORDER_CLOSE_BUTTON = ('id', 'com.hpbr.bosszhipin:id/iv_close')
    # 订单提示文本（resource-id="com.hpbr.bosszhipin:id/tv_tip"）
    ORDER_TIP_TEXT = ('id', 'com.hpbr.bosszhipin:id/tv_tip')
    # 订单卡片姓名（resource-id="com.hpbr.bosszhipin:id/tv_name"）
    ORDER_CARD_NAME = ('id', 'com.hpbr.bosszhipin:id/tv_name')
    # 订单卡片职位信息（resource-id="com.hpbr.bosszhipin:id/tv_info"）
    ORDER_CARD_INFO = ('id', 'com.hpbr.bosszhipin:id/tv_info')
    # 订单卡片公司与职位（resource-id="com.hpbr.bosszhipin:id/tv_exp"）
    ORDER_CARD_EXP = ('id', 'com.hpbr.bosszhipin:id/tv_exp')
    # 订单卡片学历（resource-id="com.hpbr.bosszhipin:id/tv_edu"）
    ORDER_CARD_EDU = ('id', 'com.hpbr.bosszhipin:id/tv_edu')
    # 订单卡片状态（resource-id="com.hpbr.bosszhipin:id/cl_status"）
    ORDER_CARD_STATUS = ('id', 'com.hpbr.bosszhipin:id/cl_status')
    # 订单卡片沟通状态（resource-id="com.hpbr.bosszhipin:id/tv_contact"）
    ORDER_CARD_CONTACT = ('id', 'com.hpbr.bosszhipin:id/tv_contact')
    # 订单卡片反馈时间（resource-id="com.hpbr.bosszhipin:id/tv_geek_status"）
    ORDER_CARD_FEEDBACK_TIME = ('id', 'com.hpbr.bosszhipin:id/tv_geek_status')
    # 订单卡片头像（resource-id="com.hpbr.bosszhipin:id/iv_avatar"）
    ORDER_CARD_AVATAR = ('id', 'com.hpbr.bosszhipin:id/iv_avatar')
    # 订单卡片性别（resource-id="com.hpbr.bosszhipin:id/iv_gender"）
    ORDER_CARD_GENDER = ('id', 'com.hpbr.bosszhipin:id/iv_gender')
    # 订单卡片沟通未完成状态（text="沟通未完成"）
    ORDER_CARD_UNFINISHED = ('xpath', '//android.widget.TextView[@text="沟通未完成"]')
    # 订单卡片待沟通状态（text="待沟通"）
    ORDER_CARD_WAIT_CONTACT = ('xpath', '//android.widget.TextView[@text="待沟通"]')
    # 订单卡片沟通完成状态（text="沟通完成"）
    ORDER_CARD_FINISHED = ('xpath', '//android.widget.TextView[@text="沟通完成"]')

    # ...（原有元素和方法保持不变）...

    # ============我的订单页面新增操作方法============
    def click_back_button(self):
        """
        点击返回按钮
        """
        self.click(*self.BACK_BUTTON)

    def click_order_close_button(self):
        """
        点击订单关闭按钮
        """
        self.click(*self.ORDER_CLOSE_BUTTON)

    def get_order_tip_text(self):
        """
        获取订单提示文本
        :return: str
        """
        element = self.find_element(*self.ORDER_TIP_TEXT)
        return element.text if element else None

    def get_order_card_name(self, index=1):
        """
        获取订单卡片姓名
        :param index: 第几个卡片，默认第1个
        :return: str
        """
        cards = self.find_elements(*self.ORDER_CARD_NAME)
        if cards and len(cards) >= index:
            return cards[index-1].text
        return None

    def get_order_card_info(self, index=1):
        """
        获取订单卡片职位信息
        :param index: 第几个卡片，默认第1个
        :return: str
        """
        cards = self.find_elements(*self.ORDER_CARD_INFO)
        if cards and len(cards) >= index:
            return cards[index-1].text
        return None

    def get_order_card_status(self, index=1):
        """
        获取订单卡片沟通状态
        :param index: 第几个卡片，默认第1个
        :return: str
        """
        cards = self.find_elements(*self.ORDER_CARD_CONTACT)
        if cards and len(cards) >= index:
            return cards[index-1].text
        return None
