# coding: utf-8


import xlrd
from xlutils.copy import copy
from common import interface_log, interface_config


class Excels:

    # 初始化
    def __init__(self, excel_name=None):
        # excle路径
        if excel_name:
            self.excel_name = excel_name
        else:
            self.excel_name = "../data/data.xlsx"
        self.log = interface_log.create_mylog()

    def list_dic(self, list1, list2):
        """
        多个列表(list)合并成一个dict（list1， list2）
        :param list1: 列表1
        :param list2: 列表2
        :return: 返回合并后的dict
        """
        try:
            # 使用lambda函数创建匿名函数对象并通过map映射给dict
            dic = dict(map(lambda x, y: [x, y], list1, list2))
            return dic
        except Exception as e:
            self.log.error("多个列表(list)合并成一个字典（dict）错误： %s" % e)
            raise

    def merage_cell(self, sheet_info):
        """
        合并单元格：处理合并横向单元格和合并垂直单元格，分配空单元格
        :param rlow:row，包含row范围以外的行
        :param rhigh：行范围
        :param clow:col，包含col范围以外的列
        :param chigh:col_范围
        :param sheet_info:工作表的对象
        :return:dic包含所有空单元格值
        """
        try:
            merge = {}
            # 合并单元格
            merge_cells = sheet_info.merged_cells
            # 循环遍历合并的单元格
            for (rlow, rhigh, clow, chigh) in merge_cells:
                value_mg_cell = sheet_info.cell_value(rlow, clow)
                if rhigh - rlow == 1:
                    for n in range(chigh - clow - 1):
                        merge[(rlow, clow + n + 1)] = value_mg_cell
                elif chigh - clow == 1:
                    for n in range(rhigh - rlow - 1):
                        merge[(rlow + n + 1, clow)] = value_mg_cell
            return merge
        except Exception as e:
            self.log.error("合并单元格错误%s" % e)
            raise


    def get_excel_data(self):
        """
        获取Excel数据生成.ini文件和.yaml文件
        :return: ini文件和.yaml文件
        """
        # 定义yaml和config列表
        data_case = []
        try:
            # 使用with方法打开Excel
            with xlrd.open_workbook(self.excel_name) as fp:
                # 获取Excel的sheet表列表，存储是sheet表名
                sheet_names = fp.sheet_names()
                # for 循环读取每一个sheet表的内容
                for index in sheet_names:
                    # 根据表名获取表中的所有内容，sheet_info也是列表，列表中的值是每个单元格里值
                    sheet_info = fp.sheet_by_name(index)
                    # 获取首行，我这里的首行是表头，我打算用表头作为字典的key，每一行数据对应表头的value，每一行组成一个字典
                    first_line = sheet_info.row_values(0)
                    # 这里是调用处理合并单元格的函数
                    values_merge_cell = self.merage_cell(sheet_info)
                    if index == "interface":
                        if sheet_info.nrows <= 1:
                            print("Excel表的总行数小于1")
                        else:
                            # 开始为组成字典准备数据（for循环遍历Excel数据）
                            for i in list(range(1, sheet_info.nrows)):
                                # 定义变量并赋值
                                other_line = sheet_info.row_values(i)
                                # for循环变量合并单元格的key值
                                for key in values_merge_cell.keys():
                                    # 判断key是否存在
                                    if key[0] == i:
                                        # key赋值
                                        other_line[key[1]] = values_merge_cell[key]
                                dic = self.list_dic(first_line, other_line)
                                data_case.append(dic)
                            print(data_case)
                        return data_case
        except Exception as e:
            self.log.error("使用with方法打开Excel错误:%s" % e)
            raise


if __name__ == "__main__":
    oper = Excels()
    oper.get_excel_data()