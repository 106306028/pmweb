from django.contrib import admin
from mainsite import models
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_date', 'gender', 'age', 'email', 'tel')
    search_fields = ('name',)
    ordering = ('id',)
    
class Order_listAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'date', 'amount')
    ordering = ('-date',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock', 'TL')
    search_fields = ('name',)
    ordering = ('id',)
    
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'tel')
    search_fields = ('name',)
    ordering = ('id',)
    
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cost', 'stock', 'safe_stock', 'last_date', 'EOQ', 'supplier', 'TL')
    search_fields = ('name',)
    ordering = ('id',)
    
class IntermediateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'stock', 'safe_stock', 'TL')
    search_fields = ('name',)
    ordering = ('id',)
    
class Intermediate_elementAdmin(admin.ModelAdmin):
    list_display = ('id', 'intermediate', 'ingredient', 'quantity')
    ordering = ('id',)
       
class Product_elementAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'intermediate', 'quantity')
    ordering = ('id',)
    
class Order_list_detailAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_list', 'product', 'quantity')
    ordering = ('id',)
    
class MPSAdmin(admin.ModelAdmin):
    list_display = ('id', 'mpsStr')
    ordering = ('id'),
    
    
admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.Order_list, Order_listAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Supplier, SupplierAdmin)
admin.site.register(models.Ingredient, IngredientAdmin)
admin.site.register(models.Intermediate, IntermediateAdmin)
admin.site.register(models.Intermediate_element, Intermediate_elementAdmin)
admin.site.register(models.Product_element, Product_elementAdmin)
admin.site.register(models.Order_list_detail, Order_list_detailAdmin)
admin.site.register(models.MPS, MPSAdmin)
admin.site.register(models.Product_MRP)
admin.site.register(models.inter_MRP)
admin.site.register(models.ingre_MRP)
