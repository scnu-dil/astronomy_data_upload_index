import os
from flask import Flask, render_template, request, make_response, send_from_directory
from flask import jsonify
from flask_cors import CORS
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
import json
app = Flask(__name__)
cors = CORS(app)
patch_request_class(app)  # set maximum file size, default is 16MB
import pymysql
import re
import requests
import ast

def dict_list2sql(dict_data_list: list, sql: str):
    # 批量词典数据插入转 SQL 语句
    result_sql_list = []
    for dict_data in dict_data_list:  # 列表中的每一段数据
        tup_sql = ""
        for key in dict_data:
            tup = (dict_data[key])
            tup_sql += ("'"+ str(tup) + "'" + ",")
        tup_sql = tup_sql.rstrip(',')  # 去除最后一个逗号
        tup_sql = "(" + tup_sql + ")"
        result_sql_list.append(tup_sql)
    result_sql_list = ','.join(result_sql_list)
    result_sql_list = sql %  result_sql_list
    return result_sql_list

def insert2db(cursor, insert_data: list, base_sql: str):
    # SQL插入批量数据功能
    sql = dict_list2sql(insert_data, base_sql)
    print(sql)
    # print(sql)
    # db = pymysql.connect(host="localhost",user="root", password="mysql", database="test")  # 链接数据库及表
    # cursor = db.cursor()  # 游标对象 cursor
    try:
       cursor.execute(sql)  # 执行sql语句
       # db.commit()  # 提交到数据库执行
       return True
    except:         # 如果发生错误则回滚
        print("execute error...")
        return False
    #    db.rollback()
    # db.close()  # 关闭数据库连接

def table_exists(cursor, db_table, *createTable):
    """判断数据表是否存在"""
    sql = "show tables;"
    # db = pymysql.connect(host="localhost",user="root", password="mysql", database="test")  # 链接数据库及表
    # cursor = db.cursor()  # 游标对象 cursor
    cursor.execute(sql)
    tables = [cursor.fetchall()]
    tables_list = re.findall('(\'.*?\')', str(tables))
    tables_list = [re.sub("'", '', each) for each in tables_list]
    if db_table in tables_list:
        print("database exists")
    else:
        print("Table not found, and now is creating your tables...")
        try:
            sql = createTable[0]
            cursor.execute(sql)
            # db.commit()
            print("Successfully added table")
        except:
            # db.rollback()
            print("UnSuccessfully added table")

@app.route('/put', methods=['GET', 'POST'])
def home():
    flag = 1
    input_text = request.get_data()  # 获取前端的json格式数据
    response = {
        'status': 0
    }
    dict = json.loads(input_text)
    # result = dict["params"]['input']
    result = dict['params']
    for i in range(0, len(result)):  # 去除最后一个无用字段 show
        del result[i]['show']
        result[i]['tsHash'] = "5cecf95dabd55747f18c5c6d7f2"
    print(result)
    for r_ in result:  # 判断输入数据是否为空
        for r in r_:
            if r_[r] == '':
                response['status'] = 0
                flag = 0  # 为空，不执行SQL插入语句
                break
    if flag:
        db_table = "aa"
        base_sql = """insert into {} values %s;""".format(db_table)  # 指定SQL命令
        db = pymysql.connect(host="localhost",user="root", password="mysql", database="test")  # 链接数据库及表
        cursor = db.cursor()  # 游标对象 cursor
        table_exists(cursor, db_table)  # 判断数据表是否存在
        if insert2db(cursor, insert_data=result, base_sql=base_sql):  # SQL插入命令
            db.commit()
            response['status'] = 1  # SQL插入成功
        else:
            db.rollback()  # SQL插入失败
        db.close()

    # put_url = 'http://47.113.185.200/upload/AABCC01010'
    # mapA = {}
    # header_dict = {"Content-Type": "application/json; charset=utf8"}
    # str = json.dumps(mapA)
    # r = requests.put(put_url, data=str, headers=header_dict)
    # r = r.text
    # print(eval(r))

    return jsonify(response)  # 返回SQL插入数据状态

@app.route('/get', methods=['GET', 'POST'])
def transfer_data():
    db_table = "aa"
    query_sql = """select * from {};""".format(db_table)  # 查询命令
    db = pymysql.connect(host="localhost",user="root", password="mysql", database="test")  # 链接数据库及表
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)  # 字典格式获取数据
    table_exists(cursor, db_table)  # 判断数据表是否存在
    cursor.execute(query_sql)
    from_db_data = cursor.fetchall()  # 获取多行数据
    print(from_db_data)
    # from_db_data = [{'Element': '1', 'N_line': '2', 'O_XH': '3', 'O_XFe': '4', 'O_loge': '5', 'C_XH': '6', 'C_XFe': '7', 'C_loge': '8'}]
    response = {
        'back_data': from_db_data,
        'data_len': len(from_db_data)
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run()

