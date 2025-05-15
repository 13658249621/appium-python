#意向报告H5页面
from pages.base_page import BasePage
from utils.image_math import click_by_image

# -*- coding: utf-8 -*-
"""
意向报告页面对象
"""
class IntentionCommunicationReportPage(BasePage):


    # 查看手机按钮
    VIEW_PHONE_BUTTON = ('xpath', '//android.widget.TextView[@text="手机"]/following-sibling::*[2]')

    # 查看简历按钮，进入牛人简历详情
    VIEW_RESUME_BUTTON = ('xpath', '//android.widget.TextView[@text="查看简历"]')

    # 点击查看手机按钮
    def click_view_phone_button(self):
        self.click(*self.VIEW_PHONE_BUTTON)

    # 点击查看简历按钮
    def click_view_resume(self):
        self.click(*self.VIEW_RESUME_BUTTON)
