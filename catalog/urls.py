from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.views import home, contacts, product_info
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('catalog/<int:pk>/', product_info, name='product_info'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, )
