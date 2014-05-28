# coding=gbk

import web
from config import settings
from config import fdb
from datetime import *

db = settings.db
now = datetime.now()
settings.cntrcount
def resetcntr(cntrs):
  tcount = 0
  for cntr in cntrs:
    tcount += 1
    if cntr.LOADINGSTATUS != 'N':
      cntr.LOADINGSTATUS='��'
    else:
      cntr.LOADINGSTATUS='��'    
    if cntr.DEPARTURE == 'T':
      cntr.DEPARTURE='��'
    else:
      cntr.DEPARTURE='��'

    if cntr.ARRIVESTATUS == 'T':
      cntr.ARRIVESTATUS ='��'
    else:
      cntr.ARRIVESTATUS ='��'    
    if cntr.PODLANDSTATUS == 'T':
      cntr.PODLANDSTATUS='��'
    else:
      cntr.PODLANDSTATUS='��'
    cntr.DC = 0
    cntr.CYCLE = 0
    if (cntr.CONTRACTDATE != None): 
      cntr.CONTRACTDATE = datetime.date(cntr.CONTRACTDATE).isoformat()
#װ��    
    if (cntr.LOADINGSTATUS) == '��':
      cntr.LOADINGTIME = datetime.date(cntr.LOADINGTIME).isoformat()  
    else:
      if (cntr.POLARRIVEDTIME != None):
        cntr.LOADINGTIME = 'Ԥ��'+datetime.date(cntr.POLARRIVEDTIME).isoformat()
      else:
        cntr.LOADINGTIME = None
    
#���
    if (cntr.DEPARTURE == '��'):
      if (cntr.ATA != None):
        cntr.ETD = datetime.date(cntr.ATA).isoformat()
    else:
      if (cntr.ETD != None):
        cntr.ETD ='Ԥ��'+ datetime.date(cntr.ETD).isoformat()
      else:
        cntr.ETD =None
      
#����    
    if (cntr.ARRIVESTATUS == '��'): 
      cntr.ARRIVETIME = datetime.date(cntr.ARRIVETIME).isoformat()
    else:
      if (cntr.ETA != None): 
        cntr.ARRIVETIME = 'Ԥ��'+datetime.date(cntr.ETA).isoformat()
      else:
        cntr.ARRIVETIME = None
#�ͻ�    
    if (cntr.PODLANDSTATUS == '��'):
      cntr.PODARRIVEDTIME = datetime.date(cntr.UNLOADINGTIME).isoformat()
    else:
      if (cntr.PODARRIVEDTIME != None):
        cntr.PODARRIVEDTIME =  'Ԥ��'+datetime.date(cntr.PODARRIVEDTIME).isoformat()
      else:
        cntr.PODARRIVEDTIME = None      
  web.template.Template.globals['cntrcount'] = tcount
  print settings.cntrcount
  return cntrs


def listcntr(id,wheretext):
  db.transaction()
  st = '''
    select t.CNTRID,t.CNTRNO,t.CNTRSEAL,t.OBILLNO,t.POD,o.PODID,t.POL,t.OBILLNO,c.sname, 
    B.ETD,t.ATA,T.MBLNO,T.VSL,T.VOY,T.GOODSNAME,CON.SNAME CON,T.ORDERNO,T.DEPARTURE,
    T.LOADINGSTATUS,T.SHIPPINGSTATUS,T.ARRIVESTATUS,T.ARRIVETIME,T.PODLANDSTATUS,
    T.PODARRIVEDTIME,T.UNLOADINGTIME,t.LOADINGTIME,t.POLARRIVEDTIME,t.LOADINGWEIGHT,t.LFNO,t.ETA,o.CONTRACTDATE,t.LOTNO,O.CONTRACTNO,t.LOTNO
    from  ORDERBILLS  O 
    left join TRANSCNTR t  ON (t.SYSID=o.SYSID AND t.ENTITYID=o.ENTITYID)
    left join corps c on (c.SYSID=O.SYSID and c.corpid=O.CORPID)
    LEFT JOIN CORPS CON ON (CON.SYSID=T.SYSID AND CON.CORPID=T.REALCONEEID)
    left join goods g on (g.sysid=t.sysid and g.CName=t.GoodsName)
    left join cntrbooking b on (b.sysid=t.sysid and b.entityid=t.bookingentityid)
    where  O.SYSID=%d and O.CORPID = %d and O.CONTRACTDATE>='2014-01-01'  ''' % (1,id)
  st = st + wheretext + ' ORDER BY O.CONTRACTDATE,o.CONTRACTNO,t.CntrID'   
  cntrs = list(db.query(st))
  resetcntr(cntrs)
  return cntrs

def getcntrpod(id):	
  db.transaction()
  st = '''
    select distinct o.POD,o.PODID
    from  ORDERBILLS  O 
    where  O.SYSID=%d and O.CORPID = %d and O.CONTRACTDATE>='2014-01-01'
    ORDER BY o.POD
    ''' % (1,id)
  pods = list(db.query(st))
  return pods


def getgoodsnames(id): 
  db.transaction()
  st = '''
    select distinct t.goodsname,g.GoodsID
    from  ORDERBILLS  O 
    left join transcntr t on (t.sysid=o.sysid and t.entityid=o.entityid)
    left join goods g on (g.SysID=t.SysID and g.Cname=t.GoodsName)
    where  O.SYSID=%d and O.CORPID = %d and O.CONTRACTDATE>='2014-01-01'
    ORDER BY t.goodsname
    ''' % (1,id)
  goodsnames = list(db.query(st))
  return goodsnames

def getgoods(id):  
  db.transaction()
  st = '''
    select Cname
    from  goods
    where  sysid=%d and goodsid=%d
    ''' % (1,id)
  goodsname = list(db.query(st))
  return goodsname
