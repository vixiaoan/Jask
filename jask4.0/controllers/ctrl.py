# coding=gbk

#coding: GBK

import web
from config import settings

render = settings.render


class Index:
	def GET(self):
		return "Hello JASK"

