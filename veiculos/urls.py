from django.urls import path
from veiculos import views

urlpatterns = [
    path('veiculos/', views.veiculo_list),
    path('veiculos/<int:pk>/', views.veiculo_detail)
]