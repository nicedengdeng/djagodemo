from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from myweb.models import Types,Goods,Users,Orders,Detail
import time,json,math
def loadinfo():
    context={}
    context['type0list'] =Types.objects.filter(pid=0)
    return context
    # 商城首页
def index(request):
    context=loadinfo()
    return render(request,"myweb/index.html")
# 商城商品列表页
def list(request):
    context = loadinfo()
    list = Goods.objects.filter()
    if request.GET.get('tid','') != '':
        tid = str(request.GET.get('tid',''))
        list = list.filter(typeid__in=Types.objects.only('id').filter(path__contains=','+tid+','))
    context["goodslist"] = list
    return render(request,"myweb/list.html",context)
    
# 商城商品详情页
def detail(request,gid):
    context=loadinfo()
    ob =Goods.objects.get(id=gid)
    ob.clicknum +=1
    ob.save()
    context["goods"] = ob
    return render(request,"myweb/detail.html",context)
# 用户注册
def register(request):
	return render(request,"myweb/register.html")

#执行会员信息添加
def usersinsert(request):
    try:
        ob = Users()
        ob.username = request.POST['username']
        ob.name = "请输入用户名"
        #获取密码并md5
        import hashlib
        m = hashlib.md5() 
        m.update(bytes(request.POST['password'],encoding="utf8"))
        ob.password = m.hexdigest()
        ob.state = 1
        ob.addtime = time.time()
        ob.save()
        context = {'info':'添加成功！'}
    except:
        context = {'info':'添加失败！'}

    return render(request,"myweb/login.html",context)
# ==============后台管理员操作====================
# 会员登录
def login(request):
    return render(request,'myweb/login.html')
    # 会员登录表单
def verify(request):
    #引入随机函数模块
    import random
    from PIL import Image, ImageDraw, ImageFont
    #定义变量，用于画面的背景色、宽、高
    #bgcolor = (random.randrange(20, 100), random.randrange(
    #    20, 100),100)
    bgcolor = (242,164,247)
    width = 100
    height = 25
    #创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    #定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    #构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('static/STXIHEI.TTF', 21)
    #font = ImageFont.load_default().font
    #构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((5, -4), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, -4), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, -4), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, -4), rand_str[3], font=font, fill=fontcolor)
    #释放画笔
    del draw
    #存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    """
    python2的为
    # 内存文件操作
    import cStringIO
    buf = cStringIO.StringIO()
    """
    # 内存文件操作-->此方法为python3的
    import io
    buf = io.BytesIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')

# 会员执行登录
def dologin(request):
        # 校验验证码
    verifycode = request.session['verifycode']
    code = request.POST['code']
    if verifycode != code:
        context = {'info':'验证码错误！'}
        return render(request,"myweb/login.html",context)
    try:
        user=Users.objects.get(username=request.POST['username'])
        print(user)
        if user.state ==1:
            import hashlib
            m = hashlib.md5() 
            m.update(bytes(request.POST['password'],encoding="utf8"))
            if user.password == m.hexdigest():
                request.session['webuser']=user.toDict();
                return redirect(reverse('index'))
            else:
                context={'info':'登录密码错误'}
        else:
            context={'info':'此用户未注册'}
    except:
        context={'info':'登录账号错误！'}
    return render(request,"myweb/login.html",context)
# 会员退出
def logout(request):
    # 清除登录的session信息
    del request.session['webuser']
    # 跳转登录页面（url地址改变）
    return redirect(reverse('login'))
    # 加载登录页面(url地址不变)
    #return render(request,"myadmin/login.html")
# 购物车

