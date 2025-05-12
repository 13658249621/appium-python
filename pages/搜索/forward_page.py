# 同事选择页面
from pages.base_page import BasePage

class ColleagueSelectPage(BasePage):
    # 同事搜索框
    COLLEAGUE_SEARCH_BOX = ('xpath', '//android.widget.TextView[@text="搜索你的同事（姓名/职位/邮箱)"]')
    # 同事搜索输入框
    COLLEAGUE_SEARCH_INPUT = ('id', 'com.hpbr.bosszhipin:id/et_input')
    # 同事列表第一项
    FIRST_COLLEAGUE_ITEM = ('xpath', '//android.widget.ListView[@resource-id="com.hpbr.bosszhipin:id/listview"]/android.view.ViewGroup[1]')
    # 发送按钮
    SEND_BUTTON = ('id', 'com.hpbr.bosszhipin:id/btn_send')
    # 返回按钮
    BACK_BUTTON = ('id', 'com.hpbr.bosszhipin:id/iv_back')
    
    # 点击同事搜索框
    def click_colleague_search_box(self):
        self.click(*self.COLLEAGUE_SEARCH_BOX)
        
    # 输入同事搜索关键词
    def input_colleague_keyword(self, keyword):
        self.input(*self.COLLEAGUE_SEARCH_INPUT, keyword)
        
    # 点击第一个同事选项
    def click_first_colleague_item(self):
        self.click(*self.FIRST_COLLEAGUE_ITEM)
        
    # 点击发送按钮
    def click_send_button(self):
        self.click(*self.SEND_BUTTON)
        
    # 点击返回按钮
    def click_back_button(self):
        self.click(*self.BACK_BUTTON)
        
    # 切换到原生应用上下文
    def switch_to_native_context(self):
        self.driver.switch_to.context('NATIVE_APP') 