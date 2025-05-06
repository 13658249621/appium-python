# test_login.py
from time import sleep

import pytest
from pages.home_page import HomePage


@pytest.mark.smoke
def test_login(driver):

    home_page = HomePage(driver)
    sleep(8)
    home_page.click_WEIXIN_button()
    sleep(3)
        # 这里可以添加断言来验证登录结果
