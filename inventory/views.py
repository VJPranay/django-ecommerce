from django.shortcuts import render
from .models import Product
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from amazon.settings import SITE_NAME

# Create your views here.
def homepage(request):
    all_products = Product.objects.all()
    content = {
        'products' : all_products,
        'site_name' : SITE_NAME,
        'homepage_text' : 'Welcome',
        'homepage_desc' : "This is a online shopping web developed in django"
    }
    return render(request, template_name='index.html',
                  context=content)
