# coding=gbk
import web
import kinterbasdb
from datetime import *

db = web.database(dbn='firebird',db='192.168.0.7:D:\sealong\data\SLEMP-LGS-PRO.FB25',user='sealong',password='sl')

render = web.template.render('templates/',cache=False)

cntrcount = 0

config = web.storage(
    email='qdyinyanan@gmail.com',
    site_name = '杰斯克物流跟踪',
    site_desc = '',
    static = '/assets',
)

web.template.Template.globals['config']     = config
web.template.Template.globals['render']     = render
web.template.Template.globals['session']    = web.ctx.session 
web.template.Template.globals['cntrcount']  = cntrcount