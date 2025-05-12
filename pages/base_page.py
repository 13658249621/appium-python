# 基础页面类，所有页面类继承自该类
from appium.webdriver.common.appiumby import AppiumBy

import pytest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.image_math import click_by_image
from utils.logger import get_logger


class BasePage:
    def __init__(self, driver, max_retries=3, wait_time=10):
        self.driver = driver
        self.max_retries = max_retries
        self.wait_time = wait_time
        self.logger = get_logger()

    def find_element(self, by: AppiumBy, value):
        retries = 0
        while retries < self.max_retries:
            try:
                element = WebDriverWait(self.driver, self.wait_time).until(
                    EC.presence_of_element_located((by, value))
                )
                return element
            except Exception as e:
                self.logger.warning(f"第 {retries + 1} 次尝试查找元素失败：{e}")
                retries += 1
        self.logger.error(f"经过 {self.max_retries} 次尝试，仍未找到元素")
        return None

    def find_elements(self, by: AppiumBy, value):
        retries = 0
        while retries < self.max_retries:
            try:
                elements = WebDriverWait(self.driver, self.wait_time).until(
                    EC.presence_of_all_elements_located((by, value))
                )
                return elements
            except Exception as e:
                self.logger.warning(f"第 {retries + 1} 次尝试查找元素失败：{e}")
                retries += 1
        self.logger.error(f"经过 {self.max_retries} 次尝试，仍未找到元素")
    

    

    def click(self, by, value):
        retries = 0
        while retries < self.max_retries:
            try:
                element = self.find_element(by, value)
                if element:
                    element.click()
                    return
            except Exception as e:
                self.logger.warning(f"第 {retries + 1} 次尝试点击元素失败：{e}")
                retries += 1
        self.logger.error(f"经过 {self.max_retries} 次尝试，仍无法点击元素")

    def is_element_visible(self, by, value):
        element = self.find_element(by, value)
        return element is not None

    #控件输入文本
    def input(self, by, value, text):
        retries = 0
        while retries < self.max_retries:
            try:
                element = self.find_element(by, value)
                if element:
                    element.send_keys(text)
                    return
            except Exception as e:
                self.logger.warning(f"第 {retries + 1} 次尝试输入失败：{e}")
                retries += 1
        self.logger.error(f"经过 {self.max_retries} 次尝试，仍无法输入")
    

    def click_by_image_match(self, image_path):
        retries = 0
        while retries < self.max_retries:
            try:
                self.logger.info(f"第 {retries + 1} 次尝试点击图片：{image_path}")
                click_by_image(self.driver, image_path)
                return
            except Exception as e:
                self.logger.warning(f"第 {retries + 1} 次尝试点击图片失败：{e}")
                retries += 1
        self.logger.error(f"经过 {self.max_retries} 次尝试，仍无法点击图片")

    def assert_element_present(self, by, value, message=None):
        """
        断言元素是否存在
        :param by: 定位方式
        :param value: 定位值
        :param message: 断言失败时的提示信息
        """
        self.logger.info(f"断言元素存在：{by}={value}")
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
        self.logger.info(f"点击图片2：{image_path}")
        click_by_image(self.driver, image_path)
