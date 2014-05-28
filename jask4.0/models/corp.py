# coding=gbk

import web
from config import settings
from config import fdb
db = settings.db
tb = 'coprs'

def listcoprs():
	db.transaction()
	st = '''
		select c.sname,c.corpid,c.corpno,w.web_password from  web_users w
		left join corps c  on (w.sysid=c.sysid and w.corpid=c.corpid)
		where c.sysid=%d and web_password<>''

		''' % (1)
	corps = list(db.query(st))
	return corps

def search_sname(sname):
	db.transaction()
	st = '''
		select c.sname,c.corpid,c.corpno,w.web_password,w.permission from corps c 
		left join web_users w on (w.sysid=c.sysid and w.corpid=c.corpid)
		where c.sysid=%d and c.sname containing '%s' 
		''' % (1,sname)
	corps = list(db.query(st))
	return corps

def getcorp(id):
	db.transaction()
	st = '''select c.sname,c.corpid,c.corpno,w.web_password,w.permission from corps c 
		left join web_users w on (w.sysid=c.sysid and w.corpid=c.corpid)
		where c.sysid=%d and c.corpid=%d''' % (1,int(id))
	corp = list(db.query(st))
	return corp

def newuser(id,username,password,status,permission,remarks=''):
	#db.transaction()
	it = "insert into web_users (sysid,corpid,web_username,web_password,status,permission,remarks) values (%d,%d,'%s','%s','%s','%s','%s')" % (1,int(id),username,password,status,permission,'remarks')	
	fdb.insert(it)

def update(id,username,password,permission):
	ut = "update web_users set web_username='%s',web_password='%s',permission='%s' where sysid=%d and corpid=%d" % (username.encode('GBK'),password.encode('GBK'),permission.encode('GBK'),1,int(id))
	fdb.update(ut)


def checkuser(username,password):
	st = "select corpid from web_users where sysid=%d and web_username='%s' and web_password='%s'" % (1,username,password)
	db.transaction()
	corps = list(db.query(st))
	if corps:
		corpid = corps[0].CORPID
	else:
		corpid = 0
	return corpid
