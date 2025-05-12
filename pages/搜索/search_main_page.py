#搜索tab主页面
from pages.base_page import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


class SearchMainPage(BasePage):
    SEARCH_BOX = ('xpath', '//android.widget.TextView[@text="请输入公司/行业/技能等"]')
    SEARCH_INPUT = ('id', 'com.hpbr.bosszhipin:id/et_input')
    SEARCH_BUTTON = ('id', 'com.hpbr.bosszhipin:id/tv_search_action')
    
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
    # 订阅卡片(第一个)
    SUBSCRIPTION_CARD = ('xpath', '(//android.view.ViewGroup[@resource-id="com.hpbr.bosszhipin:id/cl_subscribe_card"])[1]')

    def click_search_box(self):
        self.click(*self.SEARCH_BOX)

    def input_search_keyword(self, keyword):
        self.input(*self.SEARCH_INPUT, keyword)

    def click_search_button(self):
        self.click(*self.SEARCH_BUTTON)
        
    # 点击我的订阅tab
    def click_my_subscription_tab(self):
        self.click(*self.MY_SUBSCRIPTION_TAB)
        
    # 点击关闭订阅按钮
    def click_close_subscription_button(self):
        self.click(*self.CLOSE_SUBSCRIPTION_BUTTON)
        
    # 点击确认按钮
    def click_confirm_positive_button(self):
        self.click(*self.CONFIRM_POSITIVE_BUTTON)
        
    # 从右往左滑动(取消订阅后创建新订阅)
    def swipe_right_to_left(self):
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(922, 623)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(328, 614)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        
    # 点击订阅按钮
    def click_subscribe_button(self):
        self.click(*self.SUBSCRIBE_BUTTON)
        
    # 获取订阅卡片上的描述文本
    def get_subscription_desc_text(self):
        element = self.find_element(*self.SUBSCRIPTION_DESC_TEXT)
        if element:
            return element.get_attribute('text')
        return None
        
    # 点击订阅卡片
    def click_subscription_card(self):
        cards = self.driver.find_elements(*self.SUBSCRIPTION_CARD)
        if cards and len(cards) > 0:
            cards[0].click()
            
    # 获取搜索框文本
    def get_search_input_text(self):
        element = self.find_element(*self.SEARCH_INPUT)
        if element:
            return element.get_attribute('text')
        return None
        
    # 验证搜索词是否在订阅描述中
    def verify_search_text_in_subscription(self):
        search_text = self.get_search_input_text()
        subscription_text = self.get_subscription_desc_text()
        assert search_text in subscription_text, f"文本不匹配: {search_text} not in {subscription_text}"

