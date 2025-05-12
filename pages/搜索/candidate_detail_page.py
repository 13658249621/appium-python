# 牛人详情页面(搜索模块)
from pages.base_page import BasePage

class CandidateDetailPage(BasePage):
    # 收藏图标按钮
    FAVORITE_BUTTON = ('xpath', '(//android.widget.ImageView[@resource-id="com.hpbr.bosszhipin:id/iv_icon"])[1]')
    # 分享按钮
    FORWARD_PARENT = ('xpath', '(//android.view.ViewGroup[@resource-id="com.hpbr.bosszhipin:id/cl_parent"])[2]')
    # 选择其他同事按钮
    SELECT_OTHER_BUTTON = ('xpath', '//android.widget.TextView[@resource-id="com.hpbr.bosszhipin:id/forwardName" and @text="选择其他"]')
    
    # 点击收藏按钮
    def click_favorite_button(self):
        self.click(*self.FAVORITE_BUTTON)
        
    # 点击分享按钮
    def click_forward_parent(self):
        self.click(*self.FORWARD_PARENT)
        
    # 点击选择其他同事按钮
    def click_select_other_button(self):
        self.click(*self.SELECT_OTHER_BUTTON) 