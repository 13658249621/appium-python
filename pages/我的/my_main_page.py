#我的tab主页面
from pages.base_page import BasePage


class MyMainPage(BasePage):
    #意向沟通动态条入口
    YXGT_DYNAMIC_BAR = ('xpath', '//android.widget.TextView[@resource-id="com.hpbr.bosszhipin:id/tv_title" and @text="意向沟通"]')
    # 招聘道具入口
    RECRUIT_PROPS_BUTTON = ('xpath', '//android.widget.TextView[@text="招聘道具"]')

    def click_yxgt_dynamic_bar(self):
        self.click(*self.YXGT_DYNAMIC_BAR)
        
    # 点击招聘道具
    def click_recruit_props_button(self):
        self.click(*self.RECRUIT_PROPS_BUTTON)
