from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from mainsite import models
import time
import datetime
import pandas as pd # for dataframes
import datetime as dt
import numpy as np
# Create your views here.
def index(request):
    template = get_template('index.html')
    html = template.render()
    return HttpResponse(html)
    

def market(request):
    template = get_template('market.html')
    html = template.render()
    return HttpResponse(html)
    
def rfm(request):
    template = get_template('rfm.html')
    user = models.user_payment_item.objects.all()[:100]
    html = template.render(locals())
    return HttpResponse(html)
    
def result(request):
    template = get_template('result.html')
    user = models.user_payment_item.objects.all()[:100]
    html = template.render(locals())
    return HttpResponse(html)
    
def item(request):
    template = get_template('item.html')  

    html = template.render()
    return HttpResponse(html)
    
def trend(request):
    template = get_template('trend.html')
    html = template.render()
    return HttpResponse(html)
    
def product(request):
    template = get_template('product.html')
    html = template.render()
    return HttpResponse(html)
    
def stock(request):
    products = models.Product.objects.all()
    intermediates = models.Intermediate.objects.all()
    ingredients = models.Ingredient.objects.all()
           
    template = get_template('stock.html')
    html = template.render(locals())
    return HttpResponse(html)
    
def mps(request):
    template = get_template('mps.html')
    html = template.render()
    return HttpResponse(html)

def mpsSearch(request, id):
    template = get_template('mpsSearch.html')
    try:
        if id:
            product = models.Product.objects.get(id=id)
            
    except:
        pass
        
    try:
        need1 = request.GET.get('need1')
        need2 = request.GET.get('need2')
        order1 = request.GET.get('order1')
        order2 = request.GET.get('order2')
        order3 = request.GET.get('order3')
        order4 = request.GET.get('order4')
    except:
        need1 = None
    if need1 is not None:
        need1 = int(need1)
        need2 = int(need2)
        order1 = int(order1)
        order2 = int(order2)
        order3 = int(order3)
        order4 = int(order4)
        production = 100
        need_list = []
        order_list = [order1, order2, order3, order4, None, None, None, None]
        now_stock_list = [] 
        mps_list = []
        for i in range(4):
            need_list.append(need1)
        for i in range(4):
            need_list.append(need2)
        now_stock = int(product.stock)
        i = 0
        while i < 8:
            if order_list[i] != None:
                if order_list[i] > need_list[i]:
                    now_stock = now_stock - order_list[i]
                    if now_stock <= 0:
                        now_stock += production
                        now_stock_list.append(now_stock)
                        mps_list.append(production)
                        i += 1
                    else:
                        now_stock_list.append(now_stock)
                        mps_list.append(0)
                        i += 1
                else:
                    now_stock = now_stock - need_list[i]
                    if now_stock <= 0:
                        now_stock += production
                        now_stock_list.append(now_stock)
                        mps_list.append(production)
                        i += 1
                    else:
                        now_stock_list.append(now_stock)
                        mps_list.append(0)
                        i += 1
            else:
                now_stock = now_stock - need_list[i]
                if now_stock <= 0:
                    now_stock += production
                    now_stock_list.append(now_stock)
                    mps_list.append(production)
                    i += 1
                else:
                    now_stock_list.append(now_stock)
                    mps_list.append(0)
                    i += 1
        mps_str = ''
        for index, x in enumerate(mps_list):
            if index == 7:
                mps_str += str(x)
            else:
                mps_str += str(x) + ','
        try:
            data = models.MPS.objects.get(id=id)
        except:
            data = None
        if data :
            data.delete()
            save = models.MPS.objects.create(id=id, mpsStr=mps_str)
            save.save()
        else:
            save = models.MPS.objects.create(id=id, mpsStr=mps_str)
            save.save()
    
    html = template.render(locals())
    return HttpResponse(html)
    
def mrp(request, id):
    template = get_template('mrp.html')
    try:
        if id:
            product = models.Product.objects.get(id=id)
            mps = models.MPS.objects.get(id=id)
            mps_list = mps.mpsStr.split(',')
            intermediate = models.Intermediate.objects.filter(product__id  = id)
            flavor = intermediate[0].name
            stock = product.stock
            pre_need, pre_stock, need, receive, send = mrpCalculate(stock, mps_list, product.TL, 1)
            mrp_str = ''
            for index, x in enumerate(send):
                if index == 7:
                    mrp_str += str(x)
                else:
                    mrp_str += str(x) + ','
            try:
                data = models.Product_MRP.objects.get(id=id)
            except:
                data = None
            if data:
                data.delete()
                save = models.Product_MRP.objects.create(id=id, mrpStr=mrp_str)
                save.save()
            else:
                save = models.Product_MRP.objects.create(id=id, mrpStr=mrp_str)
                save.save()
            
            inter_mrp_list=[]
            ingre_mrp_list=[]
            for i in intermediate:
                mrp = models.Product_MRP.objects.get(id=id)
                mrp_list = mrp.mrpStr.split(',')
                element = models.Product_element.objects.get(product=product, intermediate__id =i.id)
                ingredient = models.Ingredient.objects.filter(intermediate__id = i.id)
                stock2 = i.stock
                pre_need2, pre_stock2, need2, receive2, send2 = mrpCalculate(stock2, mrp_list, i.TL, element.quantity)
                inter_mrp_list.append([i.name, pre_need2, i.stock, pre_stock2, i.TL, need2, receive2, send2])
                mrp_str2 = ''
                for index, x in enumerate(send2):
                    if index == 7:
                        mrp_str2 += str(x)
                    else:
                        mrp_str2 += str(x) + ','
                try:
                    data = models.inter_MRP.objects.get(id=i.id)
                except:
                    data = None
                if data:
                    data.delete()
                    save = models.inter_MRP.objects.create(id=i.id, mrpStr=mrp_str2)
                    save.save()
                else:
                    save = models.inter_MRP.objects.create(id=i.id, mrpStr=mrp_str2)
                    save.save()
                for j in ingredient:
                    mrp2 = models.inter_MRP.objects.get(id= i.id)
                    mrp_list2 = mrp2.mrpStr.split(',')
                    element = models.Intermediate_element.objects.get(intermediate = i, ingredient__id = j.id)
                    stock3 = j.stock
                    pre_need3, pre_stock3, need3, receive3, send3 = mrpCalculate(stock3, mrp_list2, j.TL, element.quantity)
                    ingre_mrp_list.append([j.name, pre_need3, j.stock, pre_stock3, j.TL, need3, receive3, send3])
                    mrp_str3 = ''
                    for index, x in enumerate(send3):
                        if index == 7:
                            mrp_str3 += str(x)
                        else:
                            mrp_str3 += str(x) + ','
                    try:
                        data = models.ingre_MRP.objects.get(id=j.id)
                    except:
                        data = None
                    if data:
                        data.delete()
                        save = models.ingre_MRP.objects.create(id=j.id, mrpStr=mrp_str3)
                        save.save()
                    else:
                        save = models.ingre_MRP.objects.create(id=j.id, mrpStr=mrp_str3)
                        save.save()
    except:
        pass
        
    html = template.render(locals())
    return HttpResponse(html)

def order(request, id):
    template = get_template('order.html')
    try:
        if id:
            product = models.Product.objects.get(id=id)
            ingredient = models.Ingredient.objects.all()
            order_detail = []
            for i in ingredient:
                detail = ingre_order(i)
                order_detail.append(detail)
            
    
    except:
        pass
    
    html = template.render(locals())
    return HttpResponse(html)


def mrpCalculate(stock, mps_list, TL, times):
    pre_need = []
    pre_stock = []
    need = []
    receive = []
    send = []
    for i in range(8):
        mps = int(mps_list[i]) * times
        pre_need.append(mps)
        if mps == 0 and stock != 0:
            pre_stock.append(stock)
            need.append(0)
            receive.append(0)
            send.append(0)
        elif mps == 0 and stock == 0:
            pre_stock.append(stock)
            need.append(0)
            receive.append(0)
            send.append(0)
        elif mps != 0 and stock != 0:
            if mps >= stock:
                pre_stock.append(stock)
                quantity = mps - stock
                need.append(quantity)
                receive.append(quantity)
                send.append(quantity)
                stock = 0
            else:
                pre_stock.append(stock)
                stock -= mps
                need.append(0)
                receive.append(0)
                send.append(0)
        else:
            pre_stock.append(stock)
            need.append(mps)
            receive.append(mps)
            send.append(mps)
    for i in range(TL):
        send.pop(0)
        send.append(0)
    return pre_need, pre_stock, need, receive, send
    
def ingre_order(ingredient):
    order_list = []
    if ingredient.id == 3:
        ingre_mrp = models.ingre_MRP.objects.get(id=ingredient.id)
        ingre_mrp = ingre_mrp.mrpStr.split(',')
        row = []
        for index, i in enumerate(ingre_mrp):
            time = datetime.datetime.now()
            if len(row) == 0:
                row.append(ingredient.id)
                row.append(ingredient.name)
            i = float(i)*2
            if i == 0:
                continue
            else:
                row.append(i)
                date = datetime.timedelta(days=index*7)
                n_date = time+date
                row.append(n_date.strftime('%Y-%m-%d'))
                row.append(ingredient.supplier.name)
                row.append(ingredient.supplier.tel)
                order_list.append(row)
                row = []
                row.append(None)
                row.append(None)
    
    else:
        ingre_mrp = models.ingre_MRP.objects.get(id=ingredient.id)
        ingre_mrp = ingre_mrp.mrpStr.split(',')
        row = []
        for index, i in enumerate(ingre_mrp):
            time = datetime.datetime.now()
            if len(row) == 0:
                row.append(ingredient.id)
                row.append(ingredient.name)
            i = float(i)
            if i == 0:
                continue
            else:
                row.append(i)
                date = datetime.timedelta(days=index*7)
                n_date = time+date
                row.append(n_date.strftime('%Y-%m-%d'))
                row.append(ingredient.supplier.name)
                row.append(ingredient.supplier.tel)
                order_list.append(row)
                row = []
                row.append(None)
                row.append(None)
        
    return order_list
