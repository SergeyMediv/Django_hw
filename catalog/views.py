from django.shortcuts import render

from catalog.models import Category, Product


def home(request):
    context = {
        'object_list': Product.objects.all()[:3],
        'title': 'Магазин электроники'
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name}\n{phone}\n{message}')
    return render(request, 'catalog/contacts.html')
