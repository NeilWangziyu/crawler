import pymysql
import datetime

print('Hello World')
# 打开数据库连接
config = {
    'host':'localhost',
    'user':'root',
    'password':'wzy12345',
    'database':'Test'
}
# db = pymysql.connect("localhost","root","wzy12345","Test" )
db = pymysql.connect(**config)
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)

cursor.execute("SHOW TABLES")
all_tables = cursor.fetchall()
# 使用fecthall获取所有

print('There are %d' %len(all_tables), 'in the database, they are', all_tables)

# 读取数据库
try:
    cursor.execute("desc runoob_tbl")
    filenames = cursor.fetchall()
    print("各列标签如下：")
    for filename in filenames:
        print(filename[0])
    print("----------------------------------")
    cursor.execute("SELECT * from runoob_tbl")
    result = cursor.fetchall()
    # print(result)
    for row in result:
        runoob_id = row[0]
        runoob_title = row[1]
        runoob_author = row[2]
        submission_date =row[3]
        print("runoob_id = %s ,runoob_title = %s ,runoob_author = %s ,submission_date =%s"
          %(runoob_id, runoob_title, runoob_author, submission_date))
    print("----------------------------------")
except:
    print("Error: unable to fetch data")

# 读取数据库后按照某一列排序
# try:
#     cursor.execute("SELECT * from runoob_tbl ORDER BY submission_date ASC")
#     result = cursor.fetchall()
#     for row in result:
#         runoob_id = row[0]
#         runoob_title = row[1]
#         runoob_author = row[2]
#         submission_date = row[3]
#         print('sort by submission_date')
#         print("runoob_id = %s ,runoob_title = %s ,runoob_author = %s ,submission_date =%s"
#               % (runoob_id, runoob_title, runoob_author, submission_date))
#     print('------------------------------------')
# except:
#     print("Error: unable to fetch dara.")



# 插入新数据
# 插入修改数据必须注意要roll back
# insert = """
#         insert into runoob_tbl
#         (runoob_title, runoob_author, submission_date)
#         values
#         ('学PHP','Carry', NOW());
#         """
# try:
#     cursor.execute(insert)
#     db.commit()
#     print('插入数据成功')
# except:
#     db.rollback()
#     print('插入数据失败')








# 修改数据
# update = """
#         UPDATE runoob_tbl SET runoob_title='学R' WHERE runoob_author='Alice'
#         """
# try:
#     cursor.execute(update)
#     db.commit()
#     print('修改数据成功')
# except:
#     db.rollback()
#     print('修改数据失败')




#

# 删除数据
# delete = "DELETE FROM runoob_tbl WHERE runoob_id=9"
# try:
#     cursor.execute(delete)
#     db.commit()
#     print('删除数据成功')
# except:
#     db.rollback()
#     print('删除数据失败')



#再次读取数据库
# try:
#     cursor.execute("SELECT * from runoob_tbl")
#     result = cursor.fetchall()
#     # print(result)
#     for row in result:
#         runoob_id = row[0]
#         runoob_title = row[1]
#         runoob_author = row[2]
#         submission_date =row[3]
#         print("runoob_id = %s ,runoob_title = %s ,runoob_author = %s ,submission_date =%s"
#           %(runoob_id, runoob_title, runoob_author, submission_date))
# except:
#     print("Error: unable to fetch data")

#获取column
# try:
#     cursor.execute("SHOW COLUMNS FROM runoob_tbl")
#     results = cursor.fetchall()
#     # print(results)
#     for result in results:
#         print("Field = %s ,Type = %s ,Null = %s ,Key =%s, Default = %s, Extra = %s"
#                   %(result[0], result[1], result[2], result[3], result[4], result[5]))
# except:
#     print("Error: unable to fetch data")


#添加/删除column
# try:
#     # cursor.execute("ALTER TABLE runoob_tbl ADD Test_col INT AFTER runoob_author;")
#     cursor.execute("ALTER TABLE runoob_tbl DROP Test_col;")
# except:
#     print("Error: unable to add / delet column")
#
# try:
#     cursor.execute("SHOW COLUMNS FROM runoob_tbl")
#     results = cursor.fetchall()
#     # print(results)
#     for result in results:
#         print("Field = %s ,Type = %s ,Null = %s ,Key =%s, Default = %s, Extra = %s"
#                   %(result[0], result[1], result[2], result[3], result[4], result[5]))
# except:
#     print("Error: unable to fetch data")



# order by
# try:
#     cursor.execute("SELECT * from runoob_tbl ORDER BY runoob_author ASC")
#     result = cursor.fetchall()
#     # print(result)
#     for row in result:
#         runoob_id = row[0]
#         runoob_title = row[1]
#         runoob_author = row[2]
#         submission_date =row[3]
#         print("runoob_id = %s ,runoob_title = %s ,runoob_author = %s ,submission_date =%s"
#           %(runoob_id, runoob_title, runoob_author, submission_date))
# except:
#     print("Error: unable to fetch data")


#正则表达式
# REGEXP = "select runoob_author from runoob_tbl where runoob_author REGEXP '^T';"
# # 寻找author一项以T开头
# try:
#     cursor.execute(REGEXP)
#     results = cursor.fetchall()
#     for result in results:
#         print(result)
# except:
#     print("Error: unable to fetch data")


# use like




db.close()


