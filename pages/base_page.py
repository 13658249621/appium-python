import pytest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.image_math import click_by_image


class BasePage:
    def __init__(self, driver, max_retries=3, wait_time=10):
        self.driver = driver
        self.max_retries = max_retries
        self.wait_time = wait_time

    def find_element(self, by, value):
        retries = 0
        while retries < self.max_retries:
            try:
                element = WebDriverWait(self.driver, self.wait_time).until(
                    EC.presence_of_element_located((by, value))
                )
                return element
            except Exception as e:
                print(f"第 {retries + 1} 次尝试查找元素失败：{e}")
                retries += 1
        print(f"经过 {self.max_retries} 次尝试，仍未找到元素")
        return None

    def click(self, by, value):
        retries = 0
        while retries < self.max_retries:
            try:
                element = self.find_element(by, value)
                if element:
                    element.click()
                    return
            except Exception as e:
                print(f"第 {retries + 1} 次尝试点击元素失败：{e}")
                retries += 1
        print(f"经过 {self.max_retries} 次尝试，仍无法点击元素")

    def click_by_image_match(self, image_path):
        retries = 0
        while retries < self.max_retries:
            try:
                print(f"第 {retries + 1} 次尝试点击图片：{image_path}")
                click_by_image(self.driver, image_path)
                return
            except Exception as e:
                print(f"第 {retries + 1} 次尝试点击图片失败：{e}")
                retries += 1
        print(f"经过 {self.max_retries} 次尝试，仍无法点击图片")


    def assert_element_present(self, by, value, message=None):
        """
        断言元素是否存在
        :param by: 定位方式
        :param value: 定位值
        :param message: 断言失败时的提示信息
        """
        print(f"断言元素存在：{by}={value}")
        element = self.find_element(by, value)
        if message is None:
            message = f"元素 {by}={value} 未找到"
        assert element is not None, message

    def assert_element_text(self, by, value, expected_text, message=None):
        """
        断言元素的文本内容是否符合预期
        :param by: 定位方式
        :param value: 定位值
        :param expected_text: 预期的文本内容
        :param message: 断言失败时的提示信息
        """
        element = self.find_element(by, value)
        if element:
            actual_text = element.text
            if message is None:
                message = f"元素 {by}={value} 的文本应为 {expected_text}，实际为 {actual_text}"
            assert actual_text == expected_text, message
        else:
            if message is None:
                message = f"元素 {by}={value} 未找到，无法进行文本断言"
            pytest.fail(message)


    def click_by_image_match(self, image_path):
        print(f"点击图片2：{image_path}")
        click_by_image(self.driver, image_path)
