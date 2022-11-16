from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from veiculos import views

urlpatterns = [
    path('veiculos/', views.veiculo_list),
    path('veiculos/<int:pk>/', views.veiculo_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)