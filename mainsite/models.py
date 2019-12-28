# _*_ encoding: utf-8 _*_
from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=10)
    last_date = models.DateField()
    
    def __str__(self):
        return self.name

class Order_list(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.IntegerField()
    
    def __str__(self):
        return '[%s, 購買日:%s]'%(self.customer,self.date) 

class Product(models.Model):
    name = models.CharField(max_length=10)
    price = models.IntegerField()
    stock = models.IntegerField()
    
    
    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=10)
    tel = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Intermediate(models.Model):
    name = models.CharField(max_length=10)
    stock = models.IntegerField()
    safe_stock = models.IntegerField()
    
    def __str__(self):
        return self.name
        
        
class Ingredient(models.Model):
    name = models.CharField(max_length=10)
    cost = models.IntegerField()
    stock = models.IntegerField()
    safe_stock = models.IntegerField()
    last_date = models.DateField()
    EOQ = models.FloatField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Order_list_detail(models.Model):
    order_list = models.ForeignKey(Order_list, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    def __str__(self):
        return str(self.quantity)

class Product_element(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    intermediate = models.ForeignKey(Intermediate, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    def __str__(self):
        return str(self.quantity)
        
class Intermediate_element(models.Model):
    intermediate = models.ForeignKey(Intermediate, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()
    
    def __str__(self):
        return str(self.quantity)

class MPS(models.Model):
    mpsStr = models.CharField(max_length=20)
    
    def __str__(self):
        return self.mpsStr
    
    
    
    
    
    
    