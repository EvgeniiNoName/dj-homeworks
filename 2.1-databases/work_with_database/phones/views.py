from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_param = request.GET.get('sort')
    phones_content = Phone.objects.all()
    if sort_param == 'name':
        phones_content = phones_content.order_by('name')
    elif sort_param == 'min_price':
        phones_content = phones_content.order_by('price')
    elif sort_param == 'max_price':
        phones_content = phones_content.order_by('-price')
    context = {
        'phones': phones_content
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)
