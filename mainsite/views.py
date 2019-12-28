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
                        mps_list.append(None)
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
                        mps_list.append(None)
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
                    mps_list.append(None)
                    i += 1
        mps_str = ''
        for x in mps_list:
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
    try:
        if id:
            product = models.Product.objects.get(id=id)
            
    except:
        pass
    template = get_template('mrp.html')
    html = template.render()
    return HttpResponse(html)
    
