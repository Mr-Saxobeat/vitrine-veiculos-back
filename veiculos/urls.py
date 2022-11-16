from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from veiculos import views

urlpatterns = [
    path('veiculos/', views.VeiculoList.as_view()),
    path('veiculos/<int:pk>/', views.VeiculoDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)