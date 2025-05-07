# home_page.py
from pages.base_page import BasePage


class HomePage(BasePage):
    #微信登陆
    WODE_BUTTON = ('id', 'com.hpbr.bosszhipin:id/tv_tab_4')
    YXGT_BUTTON = ('xpath', '//android.widget.TextView[@resource-id="com.hpbr.bosszhipin:id/tv_title" and @text="意向沟通"]')


    def click_WODE_button(self):
        self.click(*self.WODE_BUTTON)
    def click_YXGT_button(self):
        self.click(*self.YXGT_BUTTON)
