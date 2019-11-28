# coding: utf-8

import requests, json
from common import interface_log, interface_assert, interface_mysql
from method.run_mehton import RunMethod


class Assemble:

    def __init__(self):
        self.log = interface_log.create_mylog()
        self.asser = interface_assert.Assertions()
        self.mysql = interface_mysql.OperationMysql()
        self.run = RunMethod()

    # 执行登录用例
    def login(self, login_data):
        '''封装登录请求，返回cookies'''
        try:
            api_ip = login_data["api_ip"]  # 获取用例IP
            api_url = login_data["api_url"]  # 获取用例地址
            url = api_ip + api_url  # 拼接用例的请求地址
            method = login_data["method"]  # 获取用例的请求方式
            try:
                datas = eval(login_data["request_data"])  # 获取用例的请求参数
            except:
                datas = None
            try:
                header = eval(login_data["headers"])  # 获取用例的请求头
            except:
                header = None
            test_nub = login_data['id']  # 获取用例的编号
            print("***%s: --> 正在执行第%s条用例 ***" % (login_data["detail"], test_nub))
            print("接口的请求方式：%s,  接口的请求url:%s" % (method, url))
            print("接口的请求头部：%s" % header)
            print("接口的请求params：%s" % datas)
            try:
                res = self.run.run_main(method, url, datas, header)
                print("请求接口的实际返回结果：%s" % res)
                if self.asser.assert_in_text(res, login_data["expect"]):
                    res["result"] = "pass" + ": 接口实际返回的msg: " + res["msg"]
                else:
                    res["result"] = "fail" + ": 接口实际返回的msg: " + res["msg"]
                print("%s：--> 第 %s 条用例测试结果: %s" % (login_data["detail"], test_nub, res["result"]))
            except Exception as e:
                self.log.error("接口返回结果错误：%s" % e)
            return res
        except Exception as e:
            self.log.error("接口请求错误：%s" % e)
            return res

    # 执行接口用例
    def interface(self, test_data):
        '''封装requests请求'''
        if "登录" in test_data["detail"]:
            if "正确的账号密码" in test_data["detail"]:
                global cookies # 定义全局变量
                res = self.login(test_data) # 调用登录
                cookies= res["data"]["token_type"] + " " + res["data"]["access_token"] # 获取登录的cookies
            else:
                res = self.login(test_data)  # 调用登录
            return res
        else:
            try:
                api_ip = test_data["api_ip"]  # 获取用例IP
                api_url = test_data["api_url"]  # 获取用例地址
                url = api_ip + api_url  # 拼接用例的请求地址
                method = test_data["method"]  # 获取用例的请求方式
                try:
                    if "注册接口" in test_data["detail"]:
                        datas = eval(test_data["request_data"])
                        content = self.mysql.search_one(datas["verifyCode"])
                        datas["verifyCode"] = content[3][7:13]
                        # datas = eval(test_data["request_data"])
                    else:
                        datas = eval(test_data["request_data"])  # 获取用例的请求参数
                except:
                    datas = None
                try:
                    if test_data["is_tooken"] == "yes":
                        header = eval(test_data["headers"])  # 获取用例的请求头
                        header["Authorization"] = cookies
                    else:
                        header = eval(test_data["headers"])
                except:
                    header = None
                test_nub = test_data['id']  # 获取用例的编号
                print("***%s: --> 正在执行第%s条用例 ***" % (test_data["detail"], test_nub))
                print("接口的请求方式：%s,  接口的请求url:%s" % (method, url))
                print("接口的请求头部：%s" % header)
                print("接口的请求params：%s" % datas)
                try:
                    res = self.run.run_main(method, url, datas, header)
                    print("请求接口的实际返回结果：%s" % res)
                    if self.asser.assert_in_text(res, test_data["expect"]):
                        res["result"] = "pass" + ": 接口实际返回的msg: " + res["msg"]
                    else:
                        res["result"] = "fail" + ": 接口实际返回的msg: " + res["msg"]
                    print("%s：--> 第 %s 条用例测试结果: %s" % (test_data["detail"], test_nub, res["result"]))
                    return res
                except Exception as e:
                    self.log.error("接口返回结果错误：%s" % e)
            except Exception as e:
                self.log.error("接口请求错误：%s" % e)




if __name__ == "__main__":
    run = Assemble()
    from common.interface_excel import Excels
    data = Excels().get_excel_data()
    print(run.interface(data[12]))

