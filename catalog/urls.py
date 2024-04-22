from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.views import HomeView, CategoryDetailView, CategoriesListView, ProductDetailView, BlogCreateView, \
    BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView, ContactsView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('category_detail/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('category_list', CategoriesListView.as_view(), name='category_list'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
    path('product_update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('product_delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('blog_view/<int:pk>', BlogDetailView.as_view(), name='blog_view'),
    path('blog_edit/<int:pk>', BlogUpdateView.as_view(), name='blog_edit'),
    path('blog_delete/<int:pk>', BlogDeleteView.as_view(), name='blog_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
