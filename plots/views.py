from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Plot
import pandas as pd
from .models import Product
import json

# Create your views here.
@login_required(login_url='/login/')
def index(request):
    queryset = Product.objects.all()
    names = [obj.name for obj in queryset]
    prices = [int(obj.price) for obj in queryset]
    context = {
        'names': json.dumps(names),
        'prices': json.dumps(prices),
        'word': json.dumps(['profits']),
    }
    return render(request,'index.html',context=context)

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return render(request,'login.html')

def products(request):
    queryset = Product.objects.all()
    names = [obj.name for obj in queryset]
    prices = [int(obj.price) for obj in queryset]

    context = {
        'names': json.dumps(names),
        'prices': json.dumps(prices),
    }
    return render(request, 'chart/products.html', context)