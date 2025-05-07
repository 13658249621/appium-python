# home_page.py
from pages.base_page import BasePage
from utils.image_math import click_by_image


class YxgtMainPAge(BasePage):
    # 微信登陆
    QuanYiMingXi_BUTTON = ('xpath', '//android.widget.TextView[@resource-id="com.hpbr.bosszhipin:id/tv_action"]')
    KeYong_BUTTON = ('xpath', '//android.view.View[contains(@text, "可用")]')
    QuGouMai_BUTTON = './pages/去购买.jpg'
    LiJiGouMai_BUTTON = './pages/立即购买.jpg'

    def click_quanyimingxi_button(self):
        self.click(*self.QuanYiMingXi_BUTTON)

    def click_keyong_button(self):
        self.click(*self.KeYong_BUTTON)

    def click_yixiaohao_button(self):
        self.click(*self.YiXiaoHao_BUTTON)
