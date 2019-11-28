# coding: utf-8


import pymysql.cursors
import json
class OperationMysql:
	def __init__(self):
		self.conn = pymysql.connect(
            host='172.16.4.7',
            port=3306,
            user='root',
            passwd='affuli123',
            db='basic_server',
            charset='utf8')
		self.cur = self.conn.cursor()

	#查询一条数据
	def search_one(self,sql):
		self.cur.execute(sql)
		result = self.cur.fetchone()
		# result = json.dumps(result)
		return result

if __name__ == '__main__':
    op_mysql = OperationMysql()
    res = op_mysql.search_one("SELECT * FROM send_sms_record WHERE accept_mobile = '13510000004' ORDER BY id DESC ")[3][7:13]
    print(res)
    # code = res[3][7:13]
    # print(code)

