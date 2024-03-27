from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.models import Category, Product, Blog


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


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.name
        return context


def category_product(request, pk):
    category_ch = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'Все товары категории {category_ch.name}',
    }
    return render(request, 'catalog/category_product.html', context)


class CategoriesListView(ListView):
    model = Category
    extra_context = {
        'title': 'Каталог категорий'
    }


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'image', )
    success_url = reverse_lazy('catalog:blog_list')


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'image', )
    success_url = reverse_lazy('catalog:blog_list')


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog_list')
