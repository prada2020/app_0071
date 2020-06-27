from Base.base import Base
from Page.pageElements import PageElements


class SearchPage(Base):

    def __init__(self):
        super().__init__()

    def search_text(self, value):
        """输入搜索内容"""
        self.send_ele(PageElements.search_input_id, value)

    def search_result(self):
        """获取搜索结果"""
        results = self.search_eles(PageElements.search_result_ids)
        return [i.text for i in results]
