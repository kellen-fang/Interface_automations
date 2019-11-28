# coding: utf-8

import requests
import json


class RunMethod:

    # 封装post请求
    def post_main(self, url, data, header=None):
        res = None
        datas = json.dumps(data)
        if header != None:
            res = requests.post(url=url, data=datas, headers=header)
        else:
            res = requests.post(url=url, data=datas)
        return res.json()

    # 封装get请求
    def get_main(self, url, data=None, header=None):
        res = None
        if header != None:
            res = requests.get(url=url, params=data, headers=header, verify=True)
        else:
            res = requests.get(url=url, params=data, verify=True)
        return res.json()

    # 封装put请求
    def put_main(self, url, data, header=None):
        res = None
        # data1 = json.dumps(data)
        print(data)
        if header != None:
            res = requests.put(url=url, data=data, headers=header)
        else:
            res = requests.put(url=url, data=data)
        return res.json()

    # 封装delete请求
    def delete_main(self, url, data=None, header=None):
        res = None
        data1 = json.dumps(data)
        if header != None:
            res = requests.delete(url=url, params=data1, headers=header, verify=True)
        else:
            res = requests.delete(url=url, params=data1, verify=True)
        return res.json()

    # 运行请求方法
    def run_main(self, method, url, data=None, header=None):
        res = None
        if method == "post":
            res = self.post_main(url, data, header)
        elif method == "get":
            res = self.get_main(url, data, header)
        elif method == "put":
            res = self.put_main(url, data, header)
        else:
            res = self.delete_main(url, data, header)
        return res


if __name__ == "__main__":
    run = RunMethod()
    url = "http://172.16.4.2:8004/api-user/appUser/login"
    url2 = "http://172.16.4.2:8004/api-user/appUser/logout"
    data = {
	"phone": "13500111121",
	"password": "F5OZQc1U4/ohPGQQJLPcEJSovPdpNCigH+3pxCn5itnbWRpuiJLuW3OKZwdFFlqhXBdvW7rySkxK\n9s7/1SW8THjxQfr4yVjLurTNeuB4o8d97UFka+NQZcVpfWjBH7uJgJ+iRBuRHCPY4oxkUnT2C9yx\n27zBPuqj8JRFQIvzQTk=",
	"type": 1
        }
    data2 = None
    headers = {'Content-Type': 'application/json'}
    res = run.run_main('post', url, data, headers)
    cookies = res["data"]["token_type"] + " " + res["data"]["access_token"]
    print(res)
    print(type(res))

    headers["Authorization"] = cookies
    print(headers)
    res1 = run.run_main("post", url2, data2, headers)
    print(res1)