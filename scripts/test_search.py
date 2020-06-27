from Base.page import Page
from Base.driver import Driver
import pytest


class TestSearch:

    def teardown_class(self):
        """退出driver"""
        Driver.quit_app_driver()

    @pytest.fixture(scope="class", autouse=True)
    def click_search_btn(self):
        """点击设置页面搜索按钮 依赖一次"""
        Page.get_settingPage().click_search_btn()

    @pytest.mark.parametrize("search_text,search_result", [("1", "休眠"), ("m", "MAC地址"), ("i", "IP地址")])
    def test_search_text(self, search_text, search_result):
        """
        搜索内容测试方法
        :param search_text: 搜索内容
        :param search_result: 搜索预期包含结果
        :return:
        """
        # 输入
        Page.get_searchPage().search_text(search_text)
        # 断言
        assert search_result in Page.get_searchPage().search_result()
