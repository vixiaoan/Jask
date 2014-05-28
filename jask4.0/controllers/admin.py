# coding=gbk

import web
from config import settings
from models import user,corp

render = settings.render

class Adminlogin:
	def POST(self):
		i = web.input()
		password = i.password
		if password == 'meiyoumima@WEB':
			web.ctx.session.userid = -1
		raise web.seeother('/admin')

class View:
	def GET(self):
		if web.ctx.session.userid == -1:
			corps = corp.listcoprs()
			return render.users(corps)
		else:
			return render.adminlogin()
	def POST(self):
		i = web.input()
		corps = corp.search_sname(i.sname)
		return render.users(corps)

class Add:
	def GET(self,id):
		corps = corp.getcorp(id)
		return render.users_add(corps[0])

	def POST(self,id):
		i = web.input()
		#javascript 判断用户录入
		corp.newuser(id,i.username,i.password,'N','')		
		return web.seeother('/admin')

class Edit:
	def GET(self,id):		
		corps = corp.getcorp(id)
		return render.users_edit(corps[0])

	def POST(self,id):
		s = ''
		i = web.input()
		
		if i.has_key('contractdate'):
			s += '1'
		else:
			s += '0'

		if i.has_key('loadingtime'):
			s += '1'
		else:
			s += '0'

		if i.has_key('etd'):
			s += '1'
		else:
			s += '0'

		if i.has_key('arrivetime'):
			s += '1'
		else:
			s += '0'

		if i.has_key('podarrivedtime'):
			s += '1'
		else:
			s += '0'

		if i.has_key('con'):
			s += '1'
		else:
			s += '0'

		if i.has_key('loadingweight'):
			s += '1'
		else:
			s += '0'

		if i.has_key('orderno'):
			s += '1'
		else:
			s += '0'

		if i.has_key('lotno'):
			s += '1'
		else:
			s += '0'

		if i.has_key('lfno'):
			s += '1'
		else:
			s += '0'

		if i.has_key('pod'):
			s += '1'
		else:
			s += '0'

		if i.has_key('cntrno'):
			s += '1'
		else:
			s += '0'

		if i.has_key('cntrseal'):
			s += '1'
		else:
			s += '0'

		if i.has_key('vsl'):
			s += '1'
		else:
			s += '0'

		if i.has_key('voy'):
			s += '1'
		else:
			s += '0'

		if i.has_key('goodsname'):
			s += '1'
		else:
			s += '0'

		corp.update(id,i.username,i.password,s)		
		return web.seeother('/admin')
