from django.shortcuts import redirect
from django.core.urlresolvers import reverse

import re

class WebMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
        #print("AdminMiddleware")

    def __call__(self, request):
        # print("mymiddle!"+request.META['REMOTE_ADDR'])
        # 定义网站后台不用登录也可访问的路由url
        urllist = ['/myweb/login','/myweb/dologin','/myweb/logout','/myweb/detail','myweb/register','myweb/register','myweb/ordersform','myweb/ordersinsert']# 获取当前请求路径
        path = request.path
        #print("Hello World!"+path)
        # 判断当前请求是否是访问网站后台,并且path不在urllist中
        if re.match("/myweb",path) and (path not in urllist):
            # 判断当前用户是否没有登录
            if "webuser" not in request.session:
                # 执行登录界面跳转
                return redirect(reverse('login'))


        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.
        return response