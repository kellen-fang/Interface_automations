# coding: utf-8


import json
from common import interface_log



# 封装断言（Assert)方法
class Assertions:

    def __init__(self):
        self.log = interface_log.create_mylog()

    def assert_code(self, code, expect_code):
        """
        断言response状态码
        :param code: 实际状态码
        :param expect_code: 期望状态码
        :return:返回断言结果
        """
        try:
            assert code == expect_code
            return True
        except:
            self.log.error("状态码错误，预期的状态码是：%s，接口返回的状态码是：%s" % (expect_code, code))
            raise

    def assert_body(self, body, body_msg, expect_msg):
        """
        断言response body中是否等于预期的msg值
        :param body: 响应body
        :param body_msg: 响应body的msg
        :param expect_msg: 期望的msg
        :return: 返回断言结果
        """
        try:
            msg = body[body_msg]
            assert msg == expect_msg
            return True
        except:
            self.log.error("响应正文消息不等于预期的消息，预期的消息是：%s，响应正文消息是：%s" % (expect_msg, body_msg))
            raise

    def assert_in_text(self, body, expect_msg):
        """
        断言response body中是否包含预期的msg字符串
        :param body: 响应body
        :param body_msg: 响应body的msg
        :param expect_msg: 期望的msg
        :return: 返回断言结果
        """
        try:
            text = json.dumps(body, ensure_ascii=False)
            assert expect_msg in text
            if expect_msg in text:
                return True
            else:
                return False
        except:
            self.log.error("响应正文不包含预期的字符串，预期的字符串是：%s， 响应的正文是：%s" % (expect_msg, text))
            raise

    def assert_text(self, body, expect_msg):
        """
        断言response body中是否等于预期的msg字符串
        :param body: 响应body
        :param body_msg: 响应body的msg
        :param expect_msg: 期望的msg
        :return: 返回断言结果
        """
        try:
            assert body == expect_msg
            return True
        except:
            self.log.error("响应的正文不等于预期的字符串，预期的字符串是：%s，响应的正文是：%s" % (expect_msg, body))
            raise

    def assert_time(self, time, expect_time):
        """
        断言response body的响应时间小于预期的最大响应时间，单位：毫秒
        :param time: body的响应时间
        :param expect_time: 预期的最大响应时间
        :return: 返回断言结果
        """
        try:
            assert time < expect_time
            return True
        except:
            self.log.error("body响应时间大于等于预期时间，预期时间为：%s，响应时间为:%s" % (expect_time, time))
            raise


if __name__ == "__main__":
    run = Assertions()
    run.assert_in_text("APP用户登录", "登录")