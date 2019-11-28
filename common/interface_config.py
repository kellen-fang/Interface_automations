# coding: utf-8


import os
from common import interface_log
from configparser import ConfigParser


# 封装操作config
class Config:

    # 初始化
    def __init__(self, config_name=None):
        if config_name:
            self.config_name = config_name
        else:
            self.config_name = "../data/config_data.ini"
            # 判断config_name文件不存在则重新创建config_name文件
            if not os.path.exists(self.config_name):
                open(self.config_name, "w", encoding="utf-8")
        self.log = interface_log.create_mylog()

    def read_config(self):
        """
        读取配置文件
        :return: 读取结果
        """
        try:
            read_conf = ConfigParser()
            read_conf.read(self.config_name)
            return read_conf
        except Exception as e:
            self.log.error("读取配置文件错误：%s" % e)
            raise

    def write_config(self, secton, option, value):
        """
        写入配置文件
        :param secton: 目标节点
        :param option: 目标节点选项
        :param value: 目标节点选项值
        :return: 返回写入结果
        """
        try:
            # 读取配置文件
            read_conf = ConfigParser()
            read_conf.read(self.config_name)
            # 判断添加的目标节点是否存在:存在则直接在目标节点下写入， 否则重新添加目标节点再写入
            if secton in read_conf.sections():
                read_conf.set(secton, option, value)
                read_conf.write(open(self.config_name, "w", encoding="utf-8"))
            else:
                read_conf.add_section(secton)
                read_conf.set(secton, option, value)
                read_conf.write(open(self.config_name, "w", encoding="utf-8"))
        except Exception as e:
            self.log.error("写入配置文件: %s" % e)
            raise


if __name__ == "__main__":
    con = Config()
    res = con.read_config()
    test = res.get("email", "value_smtp_server")
    print(test)