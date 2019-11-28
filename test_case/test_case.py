# coding: utf-8


import unittest, ddt, os, requests, json
from common.interface_excel import Excels
from common.interface_assemble import Assemble
from common.interface_assert import Assertions


# 系统路径
curpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 接口测试用例路径
excel_path = os.path.join(curpath + "/data/data.xlsx")
# 调用Excel获取接口用例数据
test_data = Excels().get_excel_data()



@ddt.ddt
class Interface(unittest.TestCase):


    # 生成接口用例
    @ddt.data(*test_data)
    def test_requests(self, data):
        detail = data["detail"]
        self._testMethodDoc = detail  # 这个变量就是指定用例描述的
        res = Assemble().interface(data)
        print("断言点： %s" % data["expect"])
        print("接口的断言结果：%s" % (Assertions().assert_in_text(res, data["expect"])))


if __name__ == "__main__":
    unittest.main()