from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.views import home, contacts, product_info, category_product, CategoriesListView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('catalog/<int:pk>/', product_info, name='product_info'),
    path('catalog/category_product/<int:pk>/', category_product, name='category_product'),
    path('category_list', CategoriesListView.as_view(), name='category_list')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
