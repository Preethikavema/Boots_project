from django.shortcuts import render
from .models import Product

# Create your views here.
def product_list(request):
    if not Product.objects.exists():
        Product.objects.create(name='iphone', description='good quality', price='120000', quality='High', quantity=50)
        Product.objects.create(name='redmi', description='latest model', price='70000', quality='Medium', quantity=150)
        Product.objects.create(name='realmi', description='high performance', price='15000', quality='Low', quantity=200)
        Product.objects.create(name='oppo', description='efficiently used', price='12000', quality='Medium', quantity=80)
        Product.objects.create(name='vivo', description='great model', price='70000', quality='High', quantity=40) 
        Product.objects.create(name='IQ', description='frequently used', price='15000', quality='Low',quantity=100)
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


