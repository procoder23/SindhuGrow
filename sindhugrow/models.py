from django.db import models

# Create your models here.
class Usermaster(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=200)
    role = models.BigIntegerField()
    is_created = models.DateTimeField(auto_now_add=True)
    is_updated = models.DateTimeField(auto_now_add=True)

class Farmer(models.Model):
    user_id = models.ForeignKey(Usermaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    village = models.CharField(max_length=50)
    taluka = models.CharField(max_length=50)
    area = models.CharField(max_length=150)
    crop = models.CharField(max_length=150)

class requestFarmer(models.Model):
    user_id = models.ForeignKey(Usermaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    village = models.CharField(max_length=50)
    taluka = models.CharField(max_length=50)
    area = models.CharField(max_length=150)
    crop = models.CharField(max_length=150)
    approval = models.CharField(max_length=10,default="Pending")

class Serviceprovider(models.Model):
    user_id = models.ForeignKey(Usermaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    village = models.CharField(max_length=50)
    taluka = models.CharField(max_length=50)
    area = models.CharField(max_length=150)
    equipment = models.CharField(max_length=150)

class requestServiceprovider(models.Model):
    user_id = models.ForeignKey(Usermaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    village = models.CharField(max_length=50)
    taluka = models.CharField(max_length=50)
    area = models.CharField(max_length=150)
    equipment = models.CharField(max_length=150)
    approval = models.CharField(max_length=10,default="Pending")

class Hotelmanager(models.Model):
    user_id = models.ForeignKey(Usermaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    hotelcontact = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    taluka = models.CharField(max_length=50)
    area = models.CharField(max_length=150)
    hotelname = models.CharField(max_length=150)
    
class requestHotelmanager(models.Model):
    user_id = models.ForeignKey(Usermaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    hotelcontact = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    taluka = models.CharField(max_length=50)
    area = models.CharField(max_length=150)
    hotelname = models.CharField(max_length=150)
    approval = models.CharField(max_length=10,default="Pending")

class News(models.Model):
    news = models.CharField(max_length=500)
    is_created = models.DateTimeField(auto_now_add=True,null=True)
    is_updated = models.DateTimeField(auto_now_add=True,null=True)

class Schemes(models.Model):
    title = models.CharField(max_length=500)
    publishdate = models.DateField()
    link2 = models.CharField(max_length=50)
    is_created = models.DateTimeField(auto_now_add=True,null=True)
    is_updated = models.DateTimeField(auto_now_add=True,null=True)

class User_admin(models.Model):
    user_id = models.ForeignKey(Usermaster,on_delete=models.CASCADE,null=True,blank=True)
    email = models.EmailField(max_length=25)
    password = models.CharField(max_length=8)
    role = models.BigIntegerField(default=1)
    is_created = models.DateField()

class productDetails(models.Model):
    user_id = models.ForeignKey(Usermaster,on_delete=models.CASCADE,null=True)
    firstname = models.CharField(max_length=50,default=None)
    lastname = models.CharField(max_length=50,default=None)
    productname = models.CharField(max_length=20)
    productprice = models.IntegerField()
    quality = models.CharField(max_length=15)
    freshness = models.IntegerField(null=True)
    date = models.DateField(auto_now_add=True,null=True)
    photo = models.ImageField(upload_to="img/product")

class Request_Product(models.Model):
    user_id = models.ForeignKey(Usermaster,on_delete=models.CASCADE,null=True)
    firstname = models.CharField(max_length=50,default=None)
    lastname = models.CharField(max_length=50,default=None)
    productname = models.CharField(max_length=20)
    productprice = models.IntegerField()
    quality = models.CharField(max_length=15)
    freshness = models.IntegerField(null=True )
    date = models.DateField(auto_now_add=True,null=True)
    photo = models.ImageField(upload_to="img/product")
    status = models.CharField(max_length=10,default="Pending")

class Service_Details(models.Model):
    user_id = models.ForeignKey(Usermaster,on_delete=models.CASCADE,null=True)
    firstname = models.CharField(max_length=50,default=None)
    lastname = models.CharField(max_length=50,default=None)
    service = models.CharField(max_length=20)
    rent = models.IntegerField()
    years = models.IntegerField(null=True)
    date = models.DateField(auto_now_add=True,null=True)
    photo = models.ImageField(upload_to="img/service")

class Request_Service(models.Model):
    user_id = models.ForeignKey(Usermaster,on_delete=models.CASCADE,null=True)
    firstname = models.CharField(max_length=50,default=None)
    lastname = models.CharField(max_length=50,default=None)
    service = models.CharField(max_length=20)
    rent = models.IntegerField()
    years = models.IntegerField(null=True)
    date = models.DateField(auto_now_add=True,null=True)
    photo = models.ImageField(upload_to="img/service")
    status = models.CharField(max_length=10,default="Pending")

class HotelDetails(models.Model):
    user_id = models.ForeignKey(Usermaster,on_delete=models.CASCADE,null=True)
    firstname = models.CharField(max_length=50,default=None)
    lastname = models.CharField(max_length=50,default=None)
    hotelname = models.CharField(max_length=25)
    contact = models.IntegerField()
    requirement = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True,null=True)
    image = models.ImageField(upload_to="img/hotel",blank=True)

class Request_Hotel(models.Model):
    user_id = models.ForeignKey(Usermaster,on_delete=models.CASCADE,null=True)
    firstname = models.CharField(max_length=50,default=None)
    lastname = models.CharField(max_length=50,default=None)
    hotelname = models.CharField(max_length=25)
    contact = models.IntegerField()
    requirement = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True,null=True)
    image = models.ImageField(upload_to="img/hotel",blank=True)
    status = models.CharField(max_length=10,default="Pending")

class Product(models.Model):
    user_id = models.ForeignKey(Usermaster,on_delete=models.CASCADE,null=True)
    firstname = models.CharField(max_length=50,default=None)
    lastname = models.CharField(max_length=50,default=None)
    productname = models.CharField(max_length=20)
    productprice = models.IntegerField()
    quality = models.CharField(max_length=15)
    freshness = models.IntegerField(null=True )
    date = models.DateField(auto_now_add=True,null=True)
    photo = models.ImageField(upload_to="img/product")

    


