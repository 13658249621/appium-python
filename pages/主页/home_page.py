# -*- coding: utf-8 -*-
"""
HomePage 页面对象

封装了Boss直聘App主页的主要操作，包括tab切换等。
"""
from pages.base_page import BasePage


class HomePage(BasePage):
    """
    Boss直聘App主页页面对象
    封装主页tab的点击操作
    """

    # --- 页面元素定位符 ---
    RECOMMEND_TAB = ('id', 'com.hpbr.bosszhipin:id/tv_tab_1')  # 推荐tab
    SEARCH_TAB = ('id', 'com.hpbr.bosszhipin:id/tv_tab_2')     # 搜索tab
    MESSAGE_TAB = ('id', 'com.hpbr.bosszhipin:id/tv_tab_3')    # 消息tab
    MY_TAB = ('id', 'com.hpbr.bosszhipin:id/tv_tab_4')         # 我的tab
    

    def click_my_tab(self):
        """
        点击"我的"tab
        :return: None
        """
        self.click(*self.MY_TAB)

    def click_search_tab(self):
        """
        点击"搜索"tab
        :return: None
        """
        self.click(*self.SEARCH_TAB)

    def click_recommend_tab(self):
        """
        点击"推荐"tab
        :return: None
        """
        self.click(*self.RECOMMEND_TAB)

    def click_message_tab(self):
        """
        点击"消息"tab
        :return: None
        """
        self.click(*self.MESSAGE_TAB)
