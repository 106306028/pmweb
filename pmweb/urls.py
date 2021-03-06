"""pmweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from mainsite import views
urlpatterns = [
    url(r'^$', views.index),
    path('market/', views.market),
    path('market/rfm/', views.rfm),
    path('market/rfm/result/', views.result),
    path('market/item/', views.item),
    path('market/trend/', views.trend),
    path('product/', views.product),
    path('product/stock/', views.stock),
    path('product/mps/', views.mps),
    path('product/mps/<int:id>', views.mpsSearch),
    path('product/mps/mrp/<int:id>', views.mrp),
    path('product/order/<int:id>', views.order),
    path('admin/', admin.site.urls),
]
