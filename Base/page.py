from Page.settingPage import SettingPage
from Page.searchPage import SearchPage


class Page:
    """返回所有页面实例化对象"""

    @classmethod
    def get_settingPage(cls):
        """返回设置页面实例化对象"""
        return SettingPage()

    @classmethod
    def get_searchPage(cls):
        """返回搜索页面实例化对象"""
        return SearchPage()
