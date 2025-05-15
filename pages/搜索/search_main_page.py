# -*- coding: utf-8 -*-
"""
SearchMainPage 页面对象

封装了Boss直聘App搜索主页面的主要操作，包括搜索、订阅等。
"""
from pages.base_page import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


class SearchMainPage(BasePage):
    """
    Boss直聘App搜索主页面对象
    封装搜索、订阅等相关操作
    """

    # --- 页面元素定位符 ---
    SEARCH_BOX = ('xpath', '//android.widget.TextView[@text="请输入公司/行业/技能等"]')  # 搜索框
    SEARCH_INPUT = ('id', 'com.hpbr.bosszhipin:id/et_input')  # 搜索输入框
    SEARCH_BUTTON = ('id', 'com.hpbr.bosszhipin:id/tv_search_action')  # 搜索按钮
    
    # 我的订阅tab
    MY_SUBSCRIPTION_TAB = ('xpath', '//android.widget.TextView[@resource-id="com.hpbr.bosszhipin:id/tv_tab_name" and @text="我的订阅"]')
    # 关闭订阅按钮
    CLOSE_SUBSCRIPTION_BUTTON = ('id', 'com.hpbr.bosszhipin:id/iv_subscribe_close')
    # 取消订阅确认(是)按钮
    CONFIRM_POSITIVE_BUTTON = ('id', 'com.hpbr.bosszhipin:id/tv_positive')
    # 订阅按钮
    SUBSCRIBE_BUTTON = ('xpath', '(//android.widget.Button[@resource-id="com.hpbr.bosszhipin:id/btn_subscribe"])')
    # 订阅卡片上的描述文本
    SUBSCRIPTION_DESC_TEXT = ('xpath', '//android.widget.TextView[@resource-id="com.hpbr.bosszhipin:id/tv_subscribe_desc"]')
    #订阅卡片列表
    SUBSCRIPTION_CARD_LIST = ('xpath', '//android.view.ViewGroup[@resource-id="com.hpbr.bosszhipin:id/cl_subscribe_card"]')
    # 订阅卡片(第一个)
    SUBSCRIPTION_CARD = ('xpath', '(//android.view.ViewGroup[@resource-id="com.hpbr.bosszhipin:id/cl_subscribe_card"])[1]')
    #== 搜索 ==
    def click_search_box(self):
        """
        点击搜索框
        :return: None
        """
        self.click(*self.SEARCH_BOX)

    def input_search_keyword(self, keyword):
        """
        在搜索输入框输入关键词
        :param keyword: 搜索关键词
        :return: None
        """
        self.input(*self.SEARCH_INPUT, keyword)

    def click_search_button(self):
        """
        点击搜索按钮
        :return: None
        """
        self.click(*self.SEARCH_BUTTON)
    
    #== 我的订阅 ==
    def get_subscription_card_count(self):
        """
        获取订阅卡片数量
        :return: int
        """
        cards = self.find_elements(*self.SUBSCRIPTION_CARD_LIST)
        return len(cards) if cards else 0

    
    def click_my_subscription_tab(self):
        """
        点击我的订阅tab
        :return: None
        """
        self.click(*self.MY_SUBSCRIPTION_TAB)
        
    
    def click_close_subscription_button(self):
        """
        点击关闭订阅按钮
        :return: None
        """
        self.click(*self.CLOSE_SUBSCRIPTION_BUTTON)
        
    
    def click_confirm_positive_button(self):
        """
        点击确认按钮（取消订阅）
        :return: None
        """
        self.click(*self.CONFIRM_POSITIVE_BUTTON)
        
    # 订阅卡片区域从右往左滑动(取消订阅后创建新订阅)
    def swipe_right_to_left(self):
        """
        从右往左滑动（取消订阅后创建新订阅）
        :return: None
        """
        # 获取屏幕尺寸
        screen_size = self.driver.get_window_size()
        screen_width = screen_size['width']
        
        # 获取订阅卡片的位置
        card = self.find_element(*self.SUBSCRIPTION_CARD)
        card_location = card.location
        card_y = card_location['y']
        
        # 计算滑动的起点和终点坐标
        start_x = int(screen_width * 0.8)  # 起点x坐标为屏幕宽度的80%
        end_x = int(screen_width * 0.2)    # 终点x坐标为屏幕宽度的20%
        
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(start_x, card_y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(end_x, card_y)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        
    
    def click_subscribe_button(self):
        """
        点击订阅按钮
        :return: None
        """
        self.click(*self.SUBSCRIBE_BUTTON)
        
    
    def get_subscription_desc_text(self):
        """
        获取订阅卡片上的描述文本
        :return: str or None
        """
        element = self.find_element(*self.SUBSCRIPTION_DESC_TEXT)
        if element:
            return element.get_attribute('text')
        return None
        
    
    def click_subscription_card(self):
        """
        点击订阅卡片
        :return: None
        """
        cards = self.driver.find_elements(*self.SUBSCRIPTION_CARD)
        if cards and len(cards) > 0:
            cards[0].click()
            
    
    def get_search_input_text(self):
        """
        获取搜索输入框文本
        :return: str or None
        """
        element = self.find_element(*self.SEARCH_INPUT)
        if element:
            return element.get_attribute('text')
        return None
        
    
    def verify_search_text_in_subscription(self):
        """
        验证搜索词是否在订阅描述中
        :return: None
        """
        search_text = self.get_search_input_text()
        subscription_text = self.get_subscription_desc_text()
        assert search_text in subscription_text, f"文本不匹配: {search_text} not in {subscription_text}"

