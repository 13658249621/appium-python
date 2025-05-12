# 招聘道具页面
from pages.base_page import BasePage

class RecruitPropsPage(BasePage):
    # 我的道具tab
    MY_PROPS_TAB = ('xpath', '//android.widget.TextView[@text="我的道具"]')
    # 已使用tab
    USED_TAB = ('xpath', '//android.widget.TextView[@text="已使用"]')
    # 意向沟通筛选选项
    INTENTION_COMMUNICATION_OPTION = ('xpath', '//android.widget.TextView[@text="意向沟通"]')
    # 意向沟通畅聊版道具(第一个)
    INTENTION_CHAT_PROP = ('xpath', '(//android.widget.TextView[@text="意向沟通畅聊版"])[1]')
    # 意向沟通道具查看详情按钮
    DETAIL_BUTTON = ('xpath', '//android.widget.TextView[@text="详情"]')
    # 意向沟通已沟通牛人卡片
    DETAIL_H5_ELEMENT = ('xpath', '//android.view.View[@resource-id="app"]/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View[2]')
    
    # 点击我的道具tab
    def click_my_props_tab(self):
        self.click(*self.MY_PROPS_TAB)
        
    # 点击已使用tab
    def click_used_tab(self):
        self.click(*self.USED_TAB)
        
    # 点击意向沟通筛选选项
    def click_intention_communication_option(self):
        self.click(*self.INTENTION_COMMUNICATION_OPTION)
        
    # 点击意向沟通畅聊版道具
    def click_intention_chat_prop(self):
        self.click(*self.INTENTION_CHAT_PROP)
        
    # 点击意向沟通道具查看详情按钮
    def click_detail_button(self):
        self.click(*self.DETAIL_BUTTON)
        
    # 点击意向沟通已沟通牛人卡片
    def click_detail_h5_element(self):
        self.click(*self.DETAIL_H5_ELEMENT) 