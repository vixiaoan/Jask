#coding: GBK

import web
from config import settings
from models import corp
from models import cntr
import json

render = settings.render

class Index:
	def GET(self):
		userid = web.ctx.session.userid
		if userid:
			raise web.seeother('/show')
			
		else:
			raise web.seeother('/login')

class Login:
	def GET(self):
		return render.login('')

	def POST(self):
		i = web.input()
		username = i.username
		password = i.password
		userid = corp.checkuser(username,password)

		if userid:
			corpdes = corp.getcorp(userid)
			corpname = corpdes[0]['SNAME']
			web.ctx.session.userid = userid
			web.ctx.session.username = username
			web.ctx.session.usercname = corpname
			web.ctx.session.permission = corpdes[0]['PERMISSION']
			raise web.seeother('/')			
		else:
			web.ctx.session.userid = 0
			return render.login('�û�����������������µ�¼��')

class Search:
  def GET(self):
  	return "xxx"

  def POST(self):
		
		wheretext = ''
		html = ''
		userid = web.ctx.session.userid
		permission = web.ctx.session.permission
		i = web.input()
		
		orderno            = i.get('orderno',None)
		lfno               = i.get('lfno',None)
		contractdatefrom   = i.get('contractdatefrom',None)
		contractdateto     = i.get('contractdateto',None)
		loading            = i.get('loading',None)
		ship               = i.get('ship',None)
		arrived            = i.get('arrived',None)
		send               = i.get('send',None)
		goodsnameid        = i.get('goodsname',None)
		podid              = i.get('pod',0)
		transstatus        = i.get('transstatus',0)
		
		if orderno:
			wheretext += ' and t.orderno containing '+"'"+ orderno + "'"
		if lfno:
			wheretext += ' and t.lfno containing '+"'"+ lfno + "'"
		if contractdatefrom:
			wheretext += ' and o.contractdate >= '+"'"+ contractdatefrom + "'"
		if contractdateto:
			wheretext += ' and o.contractdate <= '+"'"+ contractdateto + "'"
		if loading == 'checked':
			wheretext += " and t.LOADINGSTATUS = 'T' "
		if ship == 'checked':
			wheretext += " and t.DEPARTURE = 'T' "

		if podid:
			wheretext += " and o.PODID=" + podid
		if goodsnameid:
			wheretext += " and g.GOODSID="+"'" + goodsnameid + "'"
		if int(transstatus) == 1:
			wheretext += " and t.LOADINGSTATUS = 'T' "
		elif	int(transstatus) == 2: 
			wheretext += " and t.DEPARTURE = 'T' "
		elif int(transstatus) == 3: 	
			wheretext += " and t.ARRIVESTATUS = 'T' "
		elif int(transstatus) == 4: 	
			wheretext += " and t.PODLANDSTATUS = 'T' "
		
		if int(transstatus) != 4:
			if send != 'true' :
				wheretext += " and t.PODLANDSTATUS <> 'T' "

		cntrs = cntr.listcntr(userid,wheretext)
		html = u'''
	    <table class="table table-hover table-bordered ">
	    <thead>
	    <tr>
	      '''
		if permission[0] == '1':
			html +=u'''<th width="5%">��ͬʱ��</th> '''
		if permission[1] == '1':
			html +=u'''<th width="5%">װ������</th> '''
		if permission[2] == '1':
			html +=u'''<th width="5%">�������</th> '''
		if permission[3] == '1':
			html +=u'''<th width="5%">��������</th> '''
		if permission[4] == '1':
			html +=u'''<th width="5%">ж������</th> '''
		if permission[5] == '1':
			html +=u'''<th width="5%">�ջ���</th> '''
		if permission[6] == '1':
			html +=u'''<th width="5%">����</th> '''
		if permission[7] == '1':
			html +=u'''<th width="6%">��ͬ���</th> '''
		if permission[8] == '1':
			html +=u'''<th width="3%">���</th> '''
		if permission[9] == '1':
			html +=u'''<th width="5%">��Ʊ����</th> '''
		if permission[10] == '1':
			html +=u'''<th width="3%">Ŀ�ĸ�</th> '''
		if permission[11] == '1':
			html +=u'''<th width="5%">���</th> '''
		if permission[12] == '1':
			html +=u'''<th width="5%">���</th> '''
		if permission[13] == '1':
			html +=u'''<th width="5%">����</th> '''
		if permission[14] == '1':
			html +=u'''<th width="5%">����</th> '''
		if permission[15] == '1':
			html +=u'''<th width="4%">Ʒ��</th> tr> '''
		html += ' </thead> <tbody>'  

		for cn in cntrs:
			html +='''<tr class="odd gradeX">'''
			if permission[0] == '1':
				if cn.CONTRACTDATE == None:
					html +='''<td>'''+''+'''</td>'''	
				else:
					html +='''<td style="background-color:#8cc174">'''+cn.CONTRACTDATE.decode('GBK')+'''</td>'''
			if permission[1] == '1':
				if cn.LOADINGTIME == None:
					html +='''<td>'''+''+'''</td>'''	
				else:
					html +='''<td style="background-color:#8cc174">'''+cn.LOADINGTIME.decode('GBK')+'''</td>'''
			
			if permission[2] == '1':
				if cn.ETD == None:
					html +='''<td>'''+''+'''</td>'''
				else:
					if str(cn.ETD).find('Ԥ') == -1:
						html +='''<td style="background-color:#8cc174">'''+str(cn.ETD).decode('GBK')+'''</td>'''
					else:
						html +='''<td>'''+cn.ETD.decode('GBK')+'''</td>'''	
			#����
			if permission[3] == '1':
				if cn.ARRIVETIME == None:
					html +='''<td>'''+''+'''</td>'''	
				else:
					if cn.ARRIVETIME.find('Ԥ') == -1:
						html +='''<td style="background-color:#8cc174">'''+cn.ARRIVETIME.decode('GBK')+'''</td>'''
					else:
						html +='''<td>'''+cn.ARRIVETIME.decode('GBK')+'''</td>'''
			#�ͻ�
			if permission[4] == '1':
				if cn.PODARRIVEDTIME == None:
					html +='''<td>'''+''+'''</td>'''	
				else:
					if cn.PODARRIVEDTIME.find('Ԥ') == -1:
						html +='''<td style="background-color:#8cc174">'''+cn.PODARRIVEDTIME.decode('GBK')+'''</td>'''
					else:
						html +='''<td>'''+cn.PODARRIVEDTIME.decode('GBK')+'''</td>'''	

			if permission[5] == '1':
				if cn.CON == None:
					html +='''<td>'''+''+'''</td>'''
				else:
					html +='''<td>'''+cn.CON.decode('GBK')+'''</td>'''
			if permission[6] == '1':
				html +='''<td>'''+str(cn.LOADINGWEIGHT)+'''</td>'''
			if permission[7] == '1':
				if cn.ORDERNO == None:
					html +='''<td>'''+''+'''</td>'''
				else:
					html +='''<td>'''+cn.ORDERNO+'''</td>'''
			if permission[8] == '1':
				if cn.LOTNO == None:
					html +='''<td>'''+''+'''</td>'''
				else:
					html +='''<td>'''+cn.LOTNO+'''</td>'''			
			if permission[9] == '1':
				if cn.LFNO == None:
					html +='''<td>'''+''+'''</td>'''
				else:
					html +='''<td>'''+cn.LFNO.decode('GBK')+'''</td>'''
			if permission[10] == '1':
				if cn.POD == None:
					html +='''<td>'''+''+'''</td>'''
				else:
					html +='''<td>'''+cn.POD.decode('GBK')+'''</td>'''
			if permission[11] == '1':
				if cn.CNTRNO == None:
					html +='''<td>'''+''+'''</td>'''
				else:
					html +='''<td>'''+cn.CNTRNO+'''</td>'''
			if permission[12] == '1':
				if cn.CNTRSEAL == None:
					html +='''<td>'''+''+'''</td>'''
				else:
					html +='''<td>'''+cn.CNTRSEAL+'''</td>'''
			if permission[13] == '1':
				if cn.VSL == None:
					html +='''<td>'''+''+'''</td>'''
				else:
					html +='''<td>'''+cn.VSL.decode('GBK')+'''</td>'''
			if permission[14] == '1':
				if cn.VOY == None:
					html +='''<td>'''+''+'''</td>'''
				else:
					html +='''<td>'''+cn.VOY.decode('GBK')+'''</td>'''
			if permission[15] == '1':
				if cn.GOODSNAME == None:
					html +='''<td>'''+''+'''</td>'''
				else:
					html +='''<td>'''+cn.GOODSNAME.decode('GBK')+'''</td>'''
			html +='</tr>'
		html += '''
				</tbody>
				</table>
			'''
		rels = ['',20]
		rels[0] = html
		rels[1] = web.template.Template.globals['cntrcount']
		return json.dumps(rels) # ��������ΪGBK��������� ֻ��json��ʽ�ķ����Ժ���ʾ����������ԭ����

class Logout:
	def GET(self):
		web.ctx.session.userid = 0
		web.ctx.session.username = ''
		web.ctx.session.kill()
		raise web.seeother('/login')


