# coding: GBK

import web
from config.url import urls

app = web.application(urls,globals())

session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'username': '','usercname':'','pw': '','userid':0})

def session_hook():
	web.ctx.session = session
	
app.add_processor(web.loadhook(session_hook))

application = app.wsgifunc()

#if __name__ == "__main__":
#	app.run()