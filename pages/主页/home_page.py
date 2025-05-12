# boss直聘APP主页
from pages.base_page import BasePage


class HomePage(BasePage):
    #推荐tab
    RECOMMEND_TAB = ('id', 'com.hpbr.bosszhipin:id/tv_tab_1')
    #搜索tab
    SEARCH_TAB = ('id', 'com.hpbr.bosszhipin:id/tv_tab_2')
    #消息tab
    MESSAGE_TAB = ('id', 'com.hpbr.bosszhipin:id/tv_tab_3')
    #我的tab
    MY_TAB = ('id', 'com.hpbr.bosszhipin:id/tv_tab_4')
    

    def click_my_tab(self):
        self.click(*self.MY_TAB)

    def click_search_tab(self):
        self.click(*self.SEARCH_TAB)

    def click_recommend_tab(self):
        self.click(*self.RECOMMEND_TAB)

    def click_message_tab(self):
        self.click(*self.MESSAGE_TAB)
