from django.urls import path, include
from rest_framework.routers import DefaultRouter
from veiculos import views

router = DefaultRouter()
router.register(r'veiculos', views.VeiculoViewSet, basename='veiculo')

urlpatterns = [
    path('', include(router.urls))
]