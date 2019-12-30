from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from mainsite import models
# Create your views here.
def index(request):
    template = get_template('index.html')
    html = template.render()
    return HttpResponse(html)
    

def market(request):
    template = get_template('market.html')
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
            product_element = models.Product_element.objects.filter(product__id=id)
            print(product_element)
            stock = product.stock
            pre_stock, need, receive, send = mrpCalculate(product.stock, mps_list, product.TL, 1)
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
                models.Product_MRP.objects.update(id=id, mrpStr=mrp_str)
            else:
                models.Product_MRP.objects.create(id=id, mrpStr=mrp_str)
    except:
        pass
    try:
        inter_id = request.GET.get('inter')
        if inter_id:
            intermediate = models.Intermediate.objects.get(id=inter_id)
            ingre_list = []
            mrp = models.Product_MRP.objects.get(id=product.id)
            mps_list2 = mrp.mrpStr.split(',')
            pre_stock2, need2, receive2, send2 = mrpCalculate(intermediate.stock, mps_list2, intermediate.TL, 1)
            mrp_str2 = ''
            for index, x in enumerate(send2):
                if index == 7:
                    mrp_str2 += str(x)
                else:
                    mrp_str2 += str(x) + ','
            try:
                data = models.inter_MRP.objects.get(id=inter_id)
            except:
                data = None
            if data:
                data.delete()
                save = models.inter_MRP.objects.create(id=inter_id, mrpStr=mrp_str2)
                save.save()
            else:
                save = models.inter_MRP.objects.create(id=inter_id, mrpStr=mrp_str2)
                save.save()
    except:
        pass
        
    try:
        ingre_id = request.GET.get('ingre')
        if ingre_id:
            ingredient = models.Ingredient.objects.get(id=ingre_id)
            mrp = models.inter_MRP.objects.get(id=inter_id)
            mps_list3 = mrp.mrpStr.split(',')
            pre_stock3, need3, receive3, send3 = mrpCalculate(ingredient.stock, mps_list3, ingredient.TL, intermediate_elements.quantity)
            mrp_str3 = ''
            for index, x in enumerate(send3):
                if index == 7:
                    mrp_str3 += str(x)
                else:
                    mrp_str3 += str(x) + ','
            try:
                data = models.ingre_MRP.objects.get(id=ingre_id)
            except:
                data = None
            if data:
                data.delete()
                save = models.inter_MRP.objects.create(id=inter_id, mrpStr=mrp_str2)
                save.save()
            else:
                save = models.inter_MRP.objects.create(id=inter_id, mrpStr=mrp_str2)
                save.save()
    except:
        pass
    
        
    html = template.render(locals())
    return HttpResponse(html)

def mrpCalculate(stock, mps_list, TL, times):
    pre_stock = []
    need = []
    receive = []
    send = []
    for i in range(8):
        mps = int(mps_list[i]) * times
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
        send.pop(i)
        send.append(0)
    return pre_stock, need, receive, send