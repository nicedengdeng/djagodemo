from django.conf.urls import url
from . import views,viewsgoods

urlpatterns = [
    url(r'^$',views.index,name="myadmin_index"),


    #后台用户管理
    url(r'^users$',views.usersindex,name="myadmin_usersindex"),
    url(r'^usersadd$',views.usersadd,name="myadmin_usersadd"),
    url(r'^usersinsert$',views.usersinsert,name="myadmin_usersinsert"),
    url(r'^usersdel/(?P<uid>[0-9]+)$',views.usersdel,name="myadmin_usersdel"),
    url(r'^usersedit/(?P<uid>[0-9]+)$', views.usersedit, name="myadmin_usersedit"),
    url(r'^usersupdate/(?P<uid>[0-9]+)$', views.usersupdate, name="myadmin_usersupdate"),

    # 后台管理员路由
    url(r'^login$', views.login, name="myadmin_login"),
    url(r'^dologin$', views.dologin, name="myadmin_dologin"),
    url(r'^logout$', views.logout, name="myadmin_logout"),
    url(r'^verify$', views.verify, name="myadmin_verify"), #验证码
    url(r'^type$', viewsgoods.typeindex, name="myadmin_typeindex"),
    url(r'^typeadd/(?P<tid>[0-9]+)$', viewsgoods.typeadd, name="myadmin_typeadd"),
    url(r'^typeinsert$', viewsgoods.typeinsert, name="myadmin_typeinsert"),
    url(r'^typedel/(?P<tid>[0-9]+)$', viewsgoods.typedel, name="myadmin_typedel"),
    url(r'^typeedit/(?P<tid>[0-9]+)$', viewsgoods.typeedit, name="myadmin_typeedit"),
    url(r'^typeupdate/(?P<tid>[0-9]+)$', viewsgoods.typeupdate, name="myadmin_typeupdate"),

    # 后台商品信息管理
    url(r'^goods(?P<pIndex>[0-9]+)$', viewsgoods.goodsindex, name="myadmin_goodsindex"),
    url(r'^goodsadd$', viewsgoods.goodsadd, name="myadmin_goodsadd"),
    url(r'^goodsinsert$', viewsgoods.goodsinsert, name="myadmin_goodsinsert"),
    url(r'^goodsdel/(?P<gid>[0-9]+)$', viewsgoods.goodsdel, name="myadmin_goodsdel"),
    url(r'^goodsedit/(?P<gid>[0-9]+)$', viewsgoods.goodsedit, name="myadmin_goodsedit"),
    url(r'^goodsupdate/(?P<gid>[0-9]+)$', viewsgoods.goodsupdate, name="myadmin_goodsupdate"),


    #后台订单管理
    url(r'^detail/(?P<oid>[0-9]+)$',views.detail,name = 'myadmin_detail'),
    url(r'^orderl$',views.orderl,name = 'myadmin_orderl'),
    url(r'^orderldel/(?P<oid>[0-9]+)$',views.orderldel,name = 'myadmin_orderlsdel'),
    url(r'^orderlsfh/(?P<oid>[0-9]+)$',views.orderlsfh,name = 'myadmin_orderlsfh'),




]
