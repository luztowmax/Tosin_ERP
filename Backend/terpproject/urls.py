from django.urls import path, include
from rest_framework.routers import DefaultRouter
from terpapp.views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/products/by_barcode/', ProductViewSet.as_view({'get': 'by_barcode'})),
]

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
