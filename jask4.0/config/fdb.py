# coding=gbk
import kinterbasdb

con = kinterbasdb.connect(dsn='192.168.0.7:D:\sealong\data\SLEMP-LGS-PRO.FB25', user='sealong', password='sl')

def select(sqltext):
	cur = con.cursor()
	cur.execute(sqltext)
	return cur.itermap()

def insert(sqltext):
	cur = con.cursor()
	cur.execute(sqltext)
	con.commit()	

def update(sqltext):
	cur = con.cursor()
	cur.execute(sqltext)
	con.commit()	

