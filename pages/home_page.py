# home_page.py
from pages.base_page import BasePage


class HomePage(BasePage):
    #微信登陆
    WEIXIN_BUTTON = ("id", "com.hpbr.bosszhipin:id/img_wechat_login")

    def click_WEIXIN_button(self):
        self.click(*self.WEIXIN_BUTTON)
