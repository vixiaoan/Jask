# coding=gbk

pre_fix = 'controllers.'

urls = (
	'/',										pre_fix + 'do.Index',
	'/login',								pre_fix + 'do.Login',
	'/logout',							pre_fix + 'do.Logout',
	'/show',								pre_fix + 'show.Index',
	'/adminlogin',					pre_fix + 'admin.Adminlogin',
	'/admin',								pre_fix + 'admin.View',
	'/admin/(\d+)/edit',		pre_fix + 'admin.Edit',
	'/admin/(\d+)/add',			pre_fix + 'admin.Add',
	'/search',						  pre_fix + 'do.Search',

	)