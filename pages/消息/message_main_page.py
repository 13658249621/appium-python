from pages.base_page import BasePage


class MessageMainPage(BasePage):
    """
    消息主页页面对象
    """
    #==================顶部tab模块==================
    # 顶部tab-聊天
    CHAT_TAB = ('xpath', '//android.widget.TextView[@text="聊天"]')
    # 顶部tab-互动
    INTERACT_TAB = ('xpath', '//android.widget.TextView[@text="互动"]')
    # 右上角菜单-扫码
    MENU_1_BUTTON = ('xpath', '//android.widget.LinearLayout[@resource-id="com.hpbr.bosszhipin:id/ly_menu"]/android.widget.RelativeLayout[1]')
    # 右上角菜单-查看小秘书
    MENU_2_BUTTON = ('xpath', '//android.widget.LinearLayout[@resource-id="com.hpbr.bosszhipin:id/ly_menu"]/android.widget.RelativeLayout[2]')
    # 右上角菜单-消息设置
    MENU_3_BUTTON = ('xpath', '//android.widget.LinearLayout[@resource-id="com.hpbr.bosszhipin:id/ly_menu"]/android.widget.RelativeLayout[3]')
    
    #==================聊天tab下消息分类菜单==================
    # 二级tab-全部
    ALL_TAB = ('xpath', '//android.widget.TextView[@resource-id="com.hpbr.bosszhipin:id/tv_title" and @text="全部"]')
    # 二级tab-新招呼
    GREETING_TAB = ('xpath', '//android.widget.TextView[@resource-id="com.hpbr.bosszhipin:id/tv_title" and @text="新招呼"]')
    # 二级tab-仅沟通
    COMMUNICATE_TAB = ('xpath', '//android.widget.TextView[@resource-id="com.hpbr.bosszhipin:id/tv_title" and @text="仅沟通"]')
    # 二级tab-有交换
    EXCHANGE_TAB = ('xpath', '//android.widget.TextView[@resource-id="com.hpbr.bosszhipin:id/tv_title" and @text="有交换"]')

    # 聊天各分类tab下的消息列表
    MSG_LIST_VIEW = ('id', 'com.hpbr.bosszhipin:id/recyclerView')
    # 消息item头像
    MSG_ITEM_AVATAR_IMAGE = ('id', 'com.hpbr.bosszhipin:id/iv_avatar')
    # 消息item姓名
    MSG_ITEM_NAME_TEXT = ('id', 'com.hpbr.bosszhipin:id/tv_name')
    # 消息item职位
    MSG_ITEM_POSITION_TEXT = ('id', 'com.hpbr.bosszhipin:id/tv_position')
    # 消息item时间
    MSG_ITEM_TIME_TEXT = ('id', 'com.hpbr.bosszhipin:id/tv_time')
    # 消息item状态
    MSG_ITEM_STATUS_TEXT = ('id', 'com.hpbr.bosszhipin:id/iv_msg_status')
    # 消息item内容
    MSG_ITEM_CONTENT_TEXT = ('id', 'com.hpbr.bosszhipin:id/tv_msg')

    #==================互动tab下分类菜单==================
    # 对我感兴趣
    INTERESTED_IN_ME_TAB = ('xpath', '//android.widget.TextView[@text="对我感兴趣"]')
    # 看过我
    HAVE_SEEN_ME_TAB = ('xpath', '//android.widget.TextView[@text="看过我"]')
    # 新牛人
    NEW_PERSON_TAB = ('xpath', '//android.widget.TextView[@text="新牛人"]')
    # 意向沟通
    INTENTION_COMMUNICATION_TAB = ('xpath', '//android.widget.TextView[@text="意向沟通"]')
    # 我看过
    HAVE_SEEN_ME_TAB = ('xpath', '//android.widget.TextView[@text="我看过"]')
    # ================== 操作方法 ==================


    #==顶部tab模块==
    def click_tab_chat(self):
        """点击顶部tab-聊天"""
        self.click(*self.CHAT_TAB)

    def click_tab_interact(self):
        """点击顶部tab-互动"""
        self.click(*self.INTERACT_TAB)

    def click_menu_scan(self):
        """点击右上角菜单-扫码"""
        self.click(*self.MENU_1_BUTTON)

    def click_menu_secretary(self):
        """点击右上角菜单-查看小秘书"""
        self.click(*self.MENU_2_BUTTON)

    def click_menu_setting(self):
        """点击右上角菜单-消息设置"""
        self.click(*self.MENU_3_BUTTON)

    #==聊天tab下消息分类菜单==
    def click_tab_all(self):
        """点击二级tab-全部"""
        self.click(*self.ALL_TAB)

    def click_tab_greeting(self):
        """点击二级tab-新招呼"""
        self.click(*self.GREETING_TAB)

    def click_tab_communicate(self):
        """点击二级tab-仅沟通"""
        self.click(*self.COMMUNICATE_TAB)

    def click_tab_exchange(self):
        """点击二级tab-有交换"""
        self.click(*self.EXCHANGE_TAB)
    
    #==互动tab下分类菜单==
    def click_tab_interested_in_me(self):
        """点击二级tab-对我感兴趣"""
        self.click(*self.INTERESTED_IN_ME_TAB)

    def click_tab_have_seen_me(self):
        """点击二级tab-看过我"""
        self.click(*self.HAVE_SEEN_ME_TAB)

    def click_tab_new_person(self):
        """点击二级tab-新牛人"""
        self.click(*self.NEW_PERSON_TAB)

    def click_tab_intention_communication(self):
        """点击二级tab-意向沟通"""
        self.click(*self.INTENTION_COMMUNICATION_TAB)

    def click_tab_have_seen(self):
        """点击二级tab-我看过"""
        self.click(*self.HAVE_SEEN_TAB)

