from django.contrib import admin
from mainsite import models
# Register your models here.

admin.site.register(models.Customer)
admin.site.register(models.Order_list)
admin.site.register(models.Product)
admin.site.register(models.Supplier)
admin.site.register(models.Ingredient)
admin.site.register(models.Product_element)
admin.site.register(models.Order_list_detail)