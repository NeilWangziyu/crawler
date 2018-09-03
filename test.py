import pandas
import numpy
import matplotlib.pyplot as plt
import scipy
import torch
import pymysql

print('hello world')

db = pymysql.connect("localhost","root","wzy12345","Test" )

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print ("Database version : %s " % data)

db.close()

