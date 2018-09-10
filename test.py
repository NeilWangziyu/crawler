# import pandas
# import numpy
# import matplotlib.pyplot as plt
# import scipy
# import torch
# import pymysql
#
# print('hello world')
#
# db = pymysql.connect("localhost","root","wzy12345","Test" )
#
# cursor = db.cursor()
#
# cursor.execute("SELECT VERSION()")
#
# data = cursor.fetchone()
#
# print ("Database version : %s " % data)
#
# db.close()

def extendList(val, list=[]):
    list.append(val)
    return list


list1 = extendList(10)
list2 = extendList(123, [])
list3 = extendList('a')

print("list1 = %s" % list1)
print("list2 = %s" % list2)
print("list3 = %s" % list3)


def multipliers():
    return [lambda x: i * x for i in range(4)]


print([m(2)for m in multipliers()])