from django.urls import path, include
from .views import ProductViewSet, UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
