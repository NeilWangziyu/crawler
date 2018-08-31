import pymysql

print('Hello World')
# 打开数据库连接
db = pymysql.connect("localhost","root","wzy12345","Test" )
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
    # print(filenames)
    for filename in filenames:
        print(filename[0])

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
except:
    print("Error: unable to fetch data")



db.close()

