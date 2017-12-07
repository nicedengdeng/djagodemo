from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from myweb.models import Types,Goods,Users,Orders,Detail
import time,json,math
# from myadmin.models import Users,Goods
# from myweb.models import Types,Goods,Orders
# import times
#=======测试============
#公共信息加载函数
def loadinfo():
    context={}
    context['type0list'] = Types.objects.filter(pid=0)
    return context

#浏览购物车
def shopcart(request):
    context = loadinfo()
    if 'shoplist' not in request.session:
        request.session['shoplist']={}
    return render(request,"myweb/shopcart.html",context)

def shopshow(request):
    return render(request,"myweb/shopcart.html")


#添加购物车
def shopcartadd(request,sid):
    #获取要放入购物车中的商品信息
    goods = Goods.objects.get(id=sid)
    shop = goods.toDict();
    shop['m'] = int(request.POST['m'])
    #从session获取购物车信息
    if 'shoplist' in request.session:
        shoplist = request.session['shoplist']
    else:
        shoplist = {}

    #判断此商品是否在购物车中
    if sid in shoplist:
        #商品数量加1
        shoplist[sid]['m'] += shop['m']
    else:
        #新商品添加
        shoplist[sid] = shop

    #江购物车信息放回session
    request.session['shoplist'] = shoplist
    return redirect(reverse('shopcart'))
    # return render(requset,"myweb/shopcart")

def shopcartdel(request,sid):
    shoplist = request.session['shoplist']
    del shoplist[sid]
    request.session['shoplist'] = shoplist
    return redirect(reverse('shopcart'))

def shopcartclear(request):
    context = loadinfo()
    request.session['shoplist'] = {}
    return render(request,"myweb/shopcart.html",context)

def shopcartchange(request):
    context = loadinfo()
    shoplist = request.session['shoplist']
    #获取信息]
    shopid = request.GET['sid']
    num = int(request.GET['num'])
    if num<1:
        num = 1
    shoplist[shopid]['m'] = num #更改商品数量
    request.session['shoplist'] = shoplist
    return redirect(reverse('shopcart'))
    # return render(request,"myweb/shopcart.html",context)


#============订单处理==========
#订单首页
# def ordersform(request,gids):
#     #获取要结账的商品id信息
    # ids = request.GET['gids']
#订单详情
def ordersform(request):
    #获取要结账的商品id
    ids = request.GET.get('gids','')
    if ids == '':
        return HttpResponse("请选择要结账的商品")
    gids = ids.split(',')
    #获取购物车中的商品信息
    shoplist = request.session['shoplist']
    #封装要结账的商品信息,及总金额
    orderlist = {}
    total = 0                          
    for sid in gids:                                    
        orderlist[sid] = shoplist[sid]
        total += shoplist[sid]['price']*shoplist[sid]['m'] #累积总金额
    request.session['orderlist'] = orderlist
    request.session['total'] = total
    return render(request,"myweb/orders.html")

#订单确认页
# def ordersconfirm(request):
    # return render(request,"myweb/ordersconfirm.html")

#执行订单添加
def ordersinsert(request):
    #封装订单信息,并执行添加
    orders = Orders()
    orders.uid = request.session['webuser']['id']
    orders.linkman = request.POST['linkman']
    orders.address = request.POST['address']
    orders.code = request.POST['code']
    orders.phone = request.POST['phone']
    orders.addtime = time.time()
    orders.total = request.session['total']
    orders.status = 0
    orders.save()
    #获取订单详情
    orderlist = request.session['orderlist']
    shoplist = request.session['shoplist']
    #遍历购物信息并添加
    for shop in orderlist.values():
        # del shoplist[shop['id']]
        print(shop['id'])
        detail = Detail()
        detail.orderid = orders.id
        detail.goodsid = shop['id']
        detail.name = shop['goods']
        detail.price = shop['price']
        detail.num = shop['m']
        detail.save()

    request.session['shoplist'] = shoplist
    # return HttpResponse("订单成功:订单id号："+str(orders.id))
    context={'or':orders.id}
    return render(request,"myweb/end.html",context)

def ordersinfo(request):
    pass
