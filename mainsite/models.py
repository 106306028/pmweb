# _*_ encoding: utf-8 _*_
from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=10)
    last_date = models.DateField()
    gender = models.CharField(max_length=1)
    age = models.IntegerField()
    email = models.EmailField()
    tel = models.CharField(max_length=12)
    point = models.IntegerField()
    
    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=10)
    tel = models.CharField(max_length=10)

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
    TL = models.IntegerField()
    
    def __str__(self):
        return '{0}.{1}'.format(self.id, self.name)
        
class Intermediate(models.Model):
    name = models.CharField(max_length=10)
    stock = models.IntegerField()
    safe_stock = models.IntegerField()
    TL = models.IntegerField()
    element = models.ManyToManyField(Ingredient, through='Intermediate_element')
    
    def __str__(self):
        return '{0}.{1}'.format(self.id, self.name)

class Product(models.Model):
    name = models.CharField(max_length=10)
    price = models.IntegerField()
    stock = models.IntegerField()
    TL = models.IntegerField()
    element = models.ManyToManyField(Intermediate, through='Product_element')
    
    def __str__(self):
        return '{0}.{1}'.format(self.id, self.name)
        
class Order_list(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.IntegerField()
    product = models.ManyToManyField(Product, through='Order_list_detail')
    
    def __str__(self):
        return '單號:%s, %s , %s'%(self.id,self.date,self.customer) 

class Order_list_detail(models.Model):
    order_list = models.ForeignKey(Order_list, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    

class Product_element(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    intermediate = models.ForeignKey(Intermediate, on_delete=models.CASCADE)
    quantity = models.IntegerField()
        
class Intermediate_element(models.Model):
    intermediate = models.ForeignKey(Intermediate, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()
    

class MPS(models.Model):
    mpsStr = models.CharField(max_length=20)
    
    def __str__(self):
        return self.mpsStr
    
class Product_MRP(models.Model):
    mrpStr = models.CharField(max_length=20)
    
    def __str__(self):
        return self.mrpStr
        
class inter_MRP(models.Model):
    mrpStr = models.CharField(max_length=20)
    
    def __str__(self):
        return self.mrpStr

class ingre_MRP(models.Model):
    mrpStr = models.CharField(max_length=20)
    
    def __str__(self):
        return self.mrpStr
        
class user_payment(models.Model):
    UID = models.IntegerField()
    date = models.DateTimeField(max_length=20)
    amount = models.IntegerField()
    YEAR = models.IntegerField()
    MONTH = models.IntegerField()
    DAY = models.IntegerField()
    
    def __str__(self):
        return 'UID:{0}.Payment:{1}'.format(self.id, self.payment)
    
class user_payment_item(models.Model):
    UID = models.IntegerField()
    date = models.DateTimeField(max_length=20)
    amount = models.IntegerField()
    YEAR = models.IntegerField()
    MONTH = models.IntegerField()
    DAY = models.IntegerField()
    item = models.IntegerField()
    num = models.FloatField()
    
    def __str__(self):
        return 'UID:{0}.item:{1},number:{2}'.format(self.id, self.item, self.num)
    
    
    