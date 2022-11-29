from django.db import models
from django.contrib.auth.models import User


class Area(models.Model): # area of service 
    _id = models.AutoField(primary_key=True, editable=False)
    areaName = models.CharField(max_length=20)
    createdTime = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,)
    fullName = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=50)
    area_id = models.ForeignKey(Area, on_delete=models.CASCADE, null=False)
    createdTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.userType


class Stand(models.Model): # Store 
    _id = models.AutoField(primary_key=True, editable=False)
    user_id = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    area_id = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True)
    standName = models.CharField(max_length=40)
    desc = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=50)
    image=models.ImageField(upload_to='stand_images', null=True)
    createdTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.standName


class Category(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    stand_id = models.ForeignKey(Stand, on_delete=models.CASCADE, null=True)
    categoryName = models.CharField(max_length=50, null=False, blank=True)
    fields = ['_id', 'categoryName']
    
    def __str__(self):
        return self.categoryName


class Product(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    stand_id = models.ForeignKey(Stand, on_delete=models.CASCADE, null=False)
    prodName = models.CharField(max_length=50, null=False, blank=True)
    desc = models.CharField(max_length=50, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    inStock = models.BooleanField(default=True)
    image=models.ImageField(upload_to='product_images', null=True)
    createdTime = models.DateTimeField(auto_now_add=True)
    fields = ['_id', 'prodName', 'desc', 'price']

    def __str__(self):
        return self.prodName


class Order(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    stand_id = models.ForeignKey(Stand, on_delete=models.CASCADE, null=True)
    totalPrice = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    createdTime = models.DateTimeField(auto_now_add=True)
    fields = ['_id']

    def __str__(self):
        return self._id


class OrderedProduct(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    order_id = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    prod_id = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    amount = models.SmallIntegerField()
    totalProdPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    createdTime = models.DateTimeField(auto_now_add=True)

    fields = ['_id','orederNum','category','amount']

    def __str__(self):
        return self.prodName


class DefaultImages(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    image=models.ImageField(upload_to='default_images')

    def __str__(self):
        return self.title