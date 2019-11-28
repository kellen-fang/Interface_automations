# coding: utf-8


import unittest, os, HTMLTestRunner_cn
from BeautifulReport import BeautifulReport
from common.interface_email import SendEmail


curpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
report_path = os.path.join(curpath, "report")
case_path = os.path.join(curpath , "test_case")



def add_case(casepath=case_path, rule="test*.py"):
    '''加载所有的测试用例'''
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(casepath,
                                                  pattern=rule,)
    return discover

def run_case(all_case, reportpath=report_path):
    '''执行所有的用例, 并把结果写入测试报告'''
    run = BeautifulReport(all_case)
    report_title = "接口测试报告.html"
    run.report(
        description="用例执行情况：",
        filename=report_title,
        report_dir=reportpath
    )
    SendEmail().send_main()


if __name__ == "__main__":
    all_case = add_case()
    run_case(all_case)
