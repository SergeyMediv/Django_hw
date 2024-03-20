from django.shortcuts import render

from catalog.models import Category, Product


def home(request):
    context = {
        'object_list': Product.objects.all()[:3],
        'title': 'Магазин электроники'
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    context = {
        'title': 'Контакты'
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name}\n{phone}\n{message}')
    return render(request, 'catalog/contacts.html', context)


def product_info(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'object': product,
        'title': product.name,
    }
    return render(request, 'catalog/card.html', context)
