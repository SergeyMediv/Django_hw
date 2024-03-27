from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.views import home, contacts, ProductListView, CategoriesListView, ProductDetailView, BlogCreateView, \
    BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('catalog/product_list/<int:pk>/', ProductListView.as_view(), name='product_list'),
    path('category_list', CategoriesListView.as_view(), name='category_list'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('blog_view/<int:pk>', BlogDetailView.as_view(), name='blog_view'),
    path('blog_edit/<int:pk>', BlogUpdateView.as_view(), name='blog_edit'),
    path('blog_delete/<int:pk>', BlogDeleteView.as_view(), name='blog_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
