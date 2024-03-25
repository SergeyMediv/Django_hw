from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.views import home, contacts, category_product, CategoriesListView, ProductDetailView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('catalog/category_product/<int:pk>/', category_product, name='category_product'),
    path('category_list', CategoriesListView.as_view(), name='category_list')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
