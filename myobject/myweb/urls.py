from django.conf.urls import url
from . import views,viewsorders

urlpatterns = [
    #主界链接
    url(r'^$',views.index,name="index"),
    url(r'^list$',views.list,name="list"),
    url(r'^detail(?P<gid>[0-9]+)$',views.detail,name="detail"),
    # 会员管理
    url(r'^login$',views.login,name="login"),
    url(r'^register$',views.register,name="register"),
    url(r'^usersinsert$',views.usersinsert,name="usersinsert"),
    url(r'^dologin$', views.dologin, name="dologin"),
    url(r'^logout$', views.logout, name="logout"),
    url(r'^verify$', views.verify, name="myweb_verify"), #验证码


    #购物车管理
    url(r'^shopcart$', viewsorders.shopcart, name="shopcart"),
    url(r'^shopcartadd(?P<sid>[0-9]+)$', viewsorders.shopcartadd, name="shopcartadd"),
    url(r'^shopcartdel(?P<sid>[0-9]+)$', viewsorders.shopcartdel, name="shopcartdel"),
    url(r'^shopcartclear$', viewsorders.shopcartclear, name="shopcartclear"),
    url(r'^shopcartchange$', viewsorders.shopcartchange, name="shopcartchange"),
    url(r'^shopshow$', viewsorders.shopshow, name="shopshow"),


    #订单详情管理
    url(r'^ordersform$', viewsorders.ordersform, name="ordersform"),#订单表单
    url(r'^ordersinsert$', viewsorders.ordersinsert, name="ordersinsert"),#执行表单
    url(r'^ordersinfo$', viewsorders.ordersinfo, name="ordersinfo"),#订单信息








]
