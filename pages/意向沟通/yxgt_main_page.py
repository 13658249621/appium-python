#意向沟通主页
from pages.base_page import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


class IntentionCommunicationMainPage(BasePage):
    # 权益明细按钮
    RIGHTS_DETAIL_BUTTON = ('xpath', '//android.widget.TextView[@resource-id="com.hpbr.bosszhipin:id/tv_action"]')
    # 可用按钮
    AVAILABLE_BUTTON = ('xpath', '//android.view.View[contains(@text, "可用")]')
    # 去购买图片按钮
    PURCHASE_BUTTON_IMAGE = './pages/去购买.jpg'
    # 立即购买图片按钮
    BUY_NOW_BUTTON_IMAGE = './pages/立即购买.jpg'

    # 我的订单tab
    MY_ORDER_TAB = ('xpath', '//android.widget.TextView[@text="我的订单"]')
    # 沟通中tab
    COMMUNICATING_TAB = ('xpath', '//android.widget.TextView[@resource-id="com.hpbr.bosszhipin:id/tv_title" and @text="沟通中"]')
    # 沟通完成tab
    COMMUNICATED_TAB = ('xpath', '//android.widget.TextView[@resource-id="com.hpbr.bosszhipin:id/tv_title" and @text="沟通完成"]')
    # 筛选按钮
    FILTER_BUTTON = ('id', 'com.hpbr.bosszhipin:id/tv_filter')
    # 牛人电话无法接通筛选项
    PHONE_UNREACHABLE_OPTION = ('xpath', '//android.widget.TextView[@resource-id="com.hpbr.bosszhipin:id/tv_title" and @text="牛人电话无法接通"]')
    # 牛人可联系筛选项
    CONTACTABLE_OPTION = ('xpath', '//android.widget.TextView[@resource-id="com.hpbr.bosszhipin:id/tv_title" and @text="牛人可联系"]')
    # 牛人卡片（第一个）
    FIRST_CANDIDATE_CARD = ('xpath', '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.hpbr.bosszhipin:id/rv_list"]/android.view.ViewGroup[1]')

    # 意向沟通tab
    YXGT_TAB = ('xpath', '//android.widget.TextView[@text="意向沟通"]')
    # 筛选项按钮
    FILTER_ITEM_BUTTON = ('id', 'com.hpbr.bosszhipin:id/tv_filter_item')
    # 在职-暂不考虑筛选项
    EMPLOYED_NOT_CONSIDERING_OPTION = ('xpath', '//android.widget.TextView[@resource-id="com.hpbr.bosszhipin:id/keywords_view_text" and @text="在职-暂不考虑"]')
    # 211院校筛选项
    TOP_UNIVERSITY_OPTION = ('xpath', '//android.widget.TextView[@resource-id="com.hpbr.bosszhipin:id/keywords_view_text" and @text="211院校"]')
    # 男性筛选项
    MALE_OPTION = ('xpath', '//android.widget.TextView[@resource-id="com.hpbr.bosszhipin:id/keywords_view_text" and @text="男"]')
    # 确认按钮
    CONFIRM_BUTTON = ('id', 'com.hpbr.bosszhipin:id/btn_confirm')
    # 第一个牛人卡片(发现列表)
    FIRST_CANDIDATE_ROOT = ('xpath', '(//android.view.ViewGroup[@resource-id="com.hpbr.bosszhipin:id/cl_root"])[1]')

    # 点击权益明细按钮
    def click_rights_detail_button(self):
        self.click(*self.RIGHTS_DETAIL_BUTTON)

    # 点击可用按钮
    def click_available_button(self):
        self.click(*self.AVAILABLE_BUTTON)

    # 点击去购买图片按钮
    def click_purchase_button_image(self):
        self.click_by_image_match(self.PURCHASE_BUTTON_IMAGE)

    # 点击立即购买图片按钮
    def click_buy_now_button_image(self):
        self.click_by_image_match(self.BUY_NOW_BUTTON_IMAGE)

    # 点击我的订单tab
    def click_my_order_tab(self):
        self.click(*self.MY_ORDER_TAB)

    # 点击沟通中tab
    def click_communicating_tab(self):
        self.click(*self.COMMUNICATING_TAB)

    # 点击沟通完成tab
    def click_communicated_tab(self):
        self.click(*self.COMMUNICATED_TAB)

    # 点击筛选按钮
    def click_filter_button(self):
        self.click(*self.FILTER_BUTTON)

    # 选择牛人电话无法接通筛选项
    def click_phone_unreachable_option(self):
        self.click(*self.PHONE_UNREACHABLE_OPTION)

    # 选择牛人可联系筛选项
    def click_contactable_option(self):
        self.click(*self.CONTACTABLE_OPTION)

    # 点击第一个牛人卡片
    def click_first_candidate_card(self):
        self.click(*self.FIRST_CANDIDATE_CARD)

    # 点击意向沟通tab
    def click_yxgt_tab(self):
        self.click(*self.YXGT_TAB)
        
    # 点击筛选项按钮
    def click_filter_item_button(self):
        self.click(*self.FILTER_ITEM_BUTTON)
        
    # 选择在职-暂不考虑筛选项
    def click_employed_not_considering_option(self):
        self.click(*self.EMPLOYED_NOT_CONSIDERING_OPTION)
        
    # 执行筛选项列表上下滑动操作(从下往上滑)
    def swipe_list_up(self):
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(549, 1741)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(541, 958)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        
    # 选择211院校筛选项
    def click_top_university_option(self):
        self.click(*self.TOP_UNIVERSITY_OPTION)
        
    # 选择男性筛选项
    def click_male_option(self):
        self.click(*self.MALE_OPTION)
        
    # 点击确认按钮
    def click_confirm_button(self):
        self.click(*self.CONFIRM_BUTTON)
        
    # 点击第一个牛人卡片(发现列表)
    def click_first_candidate_root(self):
        self.click(*self.FIRST_CANDIDATE_ROOT)

