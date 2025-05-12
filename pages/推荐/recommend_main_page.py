#意向沟通主页第一个tab，推荐tab，也叫牛人tab

from pages.base_page import BasePage

class RecommendMainPage(BasePage):
    """
    推荐页面(牛人tab)的页面对象
    包含顶部职位标签、筛选条件、职位类型选择和候选人列表等元素
    """
    
    # ========== 顶部职位标签栏元素 ==========
    # 职位标签容器，可能包含多个职位标签子元素
    JOB_TITLE_CONTAINER = ('id', 'com.hpbr.bosszhipin:id/title_container')
    # 职位标签通用定位(使用resource-id定位,不依赖文本),可能存在多个职位标签
    JOB_TAB_ITEM = ('xpath', '//android.widget.LinearLayout[@resource-id="com.hpbr.bosszhipin:id/title_container"]//android.widget.TextView')
    #发布职位按钮
    PUBLISH_JOB_BUTTON = ('xpath', '//android.widget.ImageView[@resource-id="com.hpbr.bosszhipin:id/iv_menu_icon"][2]')
    
    # ========== 筛选条件栏元素 ==========
    # 左侧排序按钮容器
    SORT_BUTTONS_CONTAINER = ('id', 'com.hpbr.bosszhipin:id/rv_filter_left')
    # 推荐按钮(固定文本)
    RECOMMEND_BUTTON = ('xpath', '//android.widget.TextView[@resource-id="com.hpbr.bosszhipin:id/tv_filter_text" and @text="推荐"]')
    # 最新按钮(固定文本)
    LATEST_BUTTON = ('xpath', '//android.widget.TextView[@resource-id="com.hpbr.bosszhipin:id/tv_filter_text" and @text="最新"]')
    # 城市选择按钮
    CITY_BUTTON = ('xpath', '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.hpbr.bosszhipin:id/rv_filter_right"]//android.view.ViewGroup[1]')
    # 筛选按钮(固定文本)
    FILTER_BUTTON = ('xpath', '//android.widget.TextView[@resource-id="com.hpbr.bosszhipin:id/tv_filter_text" and @text="筛选"]')
    
    
    # ========== 候选人列表元素 ==========
    # 列表容器
    CANDIDATE_LIST = ('id', 'com.hpbr.bosszhipin:id/rv_list')
    # 候选人卡片
    CANDIDATE_CARD = ('id', 'com.hpbr.bosszhipin:id/cl_geek_card')
    # 不合适按钮
    CLOSE_BUTTON = ('id', 'com.hpbr.bosszhipin:id/iv_close')
    # 头像
    AVATAR = ('id', 'com.hpbr.bosszhipin:id/iv_avatar')
    # 性别图标
    GENDER_ICON = ('id', 'com.hpbr.bosszhipin:id/iv_gender')
    # 姓名(动态文本,使用resource-id定位)
    NAME = ('id', 'com.hpbr.bosszhipin:id/tv_geek_name')
    # 活跃状态标签
    ACTIVE_STATUS = ('id', 'com.hpbr.bosszhipin:id/fl_tags')
    # 基本信息(年龄、工作年限等,动态文本)
    BASIC_INFO = ('id', 'com.hpbr.bosszhipin:id/tv_work_edu_other_desc')
    # 工作经验容器
    WORK_EXP = ('id', 'com.hpbr.bosszhipin:id/ll_work_exp')
    # 技能标签容器
    SKILL_TAGS = ('id', 'com.hpbr.bosszhipin:id/flow_layout')
    # 技能标签文本(动态文本)
    SKILL_TAG_TEXT = ('id', 'com.hpbr.bosszhipin:id/tv_tag_text')
    # 个人描述
    DESCRIPTION = ('id', 'com.hpbr.bosszhipin:id/tv_desc')
    
    # ========== 职位选择模块 ==========
    def get_job_count(self):
        """
        获取职位标签列表
        :return: 职位标签元素列表
        """
        return self.find_elements(*self.JOB_TAB_ITEM)


    def switch_job_tab(self, index):
        """
        切换职位标签
        :param index: 职位标签索引(从1开始)
        """
        job_tabs = self.find_elements(*self.JOB_TAB_ITEM)
        if index <= len(job_tabs):
            job_tabs[index-1].click()
        
    # ========== 排序方式选择模块 ==========
    def select_sort_type(self, sort_type="推荐"):
        """
        选择排序方式
        :param sort_type: 排序类型（推荐/最新）
        """
        if sort_type == "推荐":
            self.click(*self.RECOMMEND_BUTTON)
        else:
            self.click(*self.LATEST_BUTTON)
            
    # ========== 城市选择模块 ==========
    
    def click_city_button(self):
        """
        点击城市选择按钮
        """
        self.click(*self.CITY_BUTTON)
        
    # ========== 筛选条件选择模块 ==========
    def click_filter(self):
        """
        点击筛选按钮
        """
        self.click(*self.FILTER_BUTTON)
        
    def select_job_type(self, job_type):
        """
        选择职位类型
        :param job_type: 职位类型名称
        """
        locator = ('xpath', f'//android.widget.Button[@resource-id="com.hpbr.bosszhipin:id/btn_character_word" and contains(@text,"{job_type}")]')
        self.click(*locator)
        
    def close_job_type_card(self):
        """
        关闭职位类型选择卡片
        """
        self.click(*self.CLOSE_BUTTON)

    # ========== 召回牛人列表模块 ========== 
    def get_candidate_list(self):
        """
        获取候选人列表
        :return: 候选人列表
        """
        return self.find_elements(*self.CANDIDATE_CARD)

    def get_candidate_count(self):
        """
        获取候选人数量
        :return: 候选人数量
        """
        return self.find_elements(*self.CANDIDATE_CARD)

    
    def get_all_candidate_info(self):
        """
        获取列表中所有候选人的信息
        :return: 候选人信息列表
        """
        return [self.get_candidate_info(i) for i in range(len(self.get_candidate_list()))]

    
    def get_candidate_info(self, index=0):
        """
        获取列表中第x个候选人信息
        :param index: 列表中的索引(从0开始)
        :return: 候选人信息字典，包含姓名、年龄、工作经验、学历、期望薪资、技能标签和描述信息
        """
        cards = self.find_elements(*self.CANDIDATE_CARD)
        if not cards or index >= len(cards):
            return None
            
        card = cards[index]
        basic_info = self.find_element(*self.BASIC_INFO).text.split('  |  ')
        
        # 根据basic_info长度判断是否包含年龄字段
        info_dict = {
            "name": self.find_element(*self.NAME).text,
            "basic_info": self.find_element(*self.BASIC_INFO).text,  # 保留原始字段
            "skills": self.get_skill_tags(card),
            "description": self.find_element(*self.DESCRIPTION).text
        }
        
        if len(basic_info) == 4:  # 包含年龄字段
            info_dict.update({
                "age": basic_info[0],      # 年龄，如"25岁"
                "work_exp": basic_info[1],  # 工作经验，如"22年毕业，6年"
                "degree": basic_info[2],    # 学历，如"本科","大专"
                "salary": basic_info[3],    # 期望薪资，如"面议","6-10K"
            })
        else:  # 不包含年龄字段
            info_dict.update({
                "work_exp": basic_info[0],  # 工作经验，如"22年毕业，6年"
                "degree": basic_info[1],    # 学历，如"本科","大专"
                "salary": basic_info[2],    # 期望薪资，如"面议","6-10K"
            })
            
        return info_dict
    def get_skill_tags(self, card_element):
        """
        获取技能标签列表
        :param card_element: 候选人卡片元素
        :return: 技能标签列表
        """
        tags = card_element.find_elements(*self.SKILL_TAG_TEXT)
        return [tag.text for tag in tags]
    

    def click_candidate(self, index=0):
        """
        点击候选人卡片
        :param index: 列表中的索引(从0开始)
        """
        cards = self.find_elements(*self.CANDIDATE_CARD)
        if cards and index < len(cards):
            cards[index].click()
    
    