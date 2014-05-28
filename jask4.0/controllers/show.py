#coding: GBK

import web
from config import settings
from models import cntr

render = settings.render

class Index:
	def GET(self):
		userid = web.ctx.session.userid
		pods = cntr.getcntrpod(userid)
		goodsnames = cntr.getgoodsnames(userid)
		wheretext = "and t.PODLANDSTATUS <> 'T'"
		if userid:
			cntrs = cntr.listcntr(userid,wheretext)
			return render.show1(cntrs,pods,goodsnames)
		else:
			raise web.seeother('/login')
	'''
	def POST(self):
		userid = web.ctx.session.userid
		pods = cntr.getcntrpod(userid)
		wheretext = ''
		i = web.input()
		orderno            = i.get('orderno',None)
		lfno               = i.get('lfno',None)
		contractdatefrom   = i.get('contractdatefrom',None)
		contractdateto     = i.get('contractdateto',None)
		loading            = i.get('loading',None)
		ship               = i.get('ship',None)
		arrived            = i.get('arrived',None)
		send               = i.get('send',None)
		podid              = i.get('pod',0)

		if orderno:
			wheretext += ' and t.orderno containing '+"'"+ orderno + "'"
		if lfno:
			wheretext += ' and t.lfno containing '+"'"+ lfno + "'"
		if contractdatefrom:
			wheretext += ' and o.contractdate >= '+"'"+ contractdatefrom + "'"
		if contractdateto:
			wheretext += ' and o.contractdate <= '+"'"+ contractdateto + "'"
		if loading:
			wheretext += " and t.LOADINGSTATUS = 'T' "
		if ship:
			wheretext += " and t.SHIPPINGSTATUS = 'T' "
		if arrived:
			wheretext += " and t.ARRIVESTATUS = 'T' "
		if send:
			wheretext += " and t.PODLANDSTATUS = 'T' "
		if podid:
			wheretext += "and o.PODID=" + podid
		if userid:
			cntrs = cntr.listcntr(userid,wheretext)
			return render.show(cntrs,pods)
		else:
			raise web.seeother('/login')
'''

class Pod:
	def GET(self,id):
		userid = web.ctx.session.userid
		wheretext = ''
		i = web.input()
		orderno = i.get('orderno',None)
		if orderno:
			wheretext = ' and orderno='+ orderno
		if userid:
			cntrs = cntr.listcntr(userid,wheretext)
			return render.show(cntrs,pods)
		else:
			raise web.seeother('/login')

