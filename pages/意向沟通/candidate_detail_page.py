# 牛人详情页面
from pages.base_page import BasePage

class CandidateDetailPage(BasePage):
    # 帮我问意向按钮
    ASK_INTENTION_BUTTON = ('xpath', '//android.widget.Button[@text="帮我问意向"]')
    # 职位选择控件
    POSITION_SELECTOR = ('id', 'com.hpbr.bosszhipin:id/mPositionView')
    
    # 点击帮我问意向按钮
    def click_ask_intention_button(self):
        self.click(*self.ASK_INTENTION_BUTTON)
        
    # 点击职位选择控件
    def click_position_selector(self):
        self.click(*self.POSITION_SELECTOR) 