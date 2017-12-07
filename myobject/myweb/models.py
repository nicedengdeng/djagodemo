from django.db import models

#用户信息模型
class Users(models.Model):
    username = models.CharField(max_length=32)
    name = models.CharField(max_length=16)
    password = models.CharField(max_length=32)
    sex = models.IntegerField(default=1)
    address = models.CharField(max_length=255)
    code = models.CharField(max_length=6)
    phone = models.CharField(max_length=16)
    email = models.CharField(max_length=50)
    state = models.IntegerField(default=1)
    addtime = models.IntegerField()

    class Meta:
        db_table = "users"  # 更改表名
        
    def toDict(self):
        return{'id':self.id,'name':self.name,'sex':self.sex,'address':self.address,'code':self.code,'phone':self.phone,'email':self.email}


class Types(models.Model):
    name = models.CharField(max_length=32)
    pid = models.IntegerField(default=0)
    path = models.CharField(max_length=255)

    class Meta:
        db_table = "myweb_type"  # 更改表名

class Goods(models.Model):
    typeid = models.IntegerField()
    goods = models.CharField(max_length=32)
    company = models.CharField(max_length=50)
    descr = models.TextField()
    price = models.FloatField()
    picname = models.CharField(max_length=255)
    state = models.IntegerField(default=1)
    store = models.IntegerField(default=0)
    num = models.IntegerField(default=0)
    clicknum = models.IntegerField(default=0)
    addtime = models.IntegerField()

    class Meta:
        db_table = "myweb_goods"  # 更改表名

    def toDict(self):
        return{'id':self.id,'goods':self.goods,'picname':self.picname,'price':self.price,'num':self.num,'store':self.store,'clicknum':self.clicknum,'m':1}

class Orders(models.Model):
    uid = models.IntegerField()
    linkman = models.CharField(max_length=32)
    address = models.CharField(max_length=255)
    code = models.CharField(max_length=6)
    phone = models.CharField(max_length=16)
    addtime = models.IntegerField()
    total = models.FloatField()
    status = models.IntegerField(default=0)
    class Meta:
        db_table = "orders" 
    def toDict(self):
        return{'id':self.id,'goods':self.goods,'picname':self.picname,'price':self.price,'num':self.num,'store':self.store,'clicknum':self.clicknum,'m':1}


class Detail(models.Model):
    orderid = models.IntegerField()
    goodsid = models.IntegerField()
    name = models.CharField(max_length=32)
    price = models.FloatField()
    num = models.IntegerField()

    class Meta:
        db_table = "detail"  # 更改表名