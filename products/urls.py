from django.urls import path
from .views import ProductsList,ProcuctDetail

app_name = 'products'

urlpatterns = [
    path('', ProductsList.as_view(),name='product_list'),
    path('<int:pk>', ProcuctDetail.as_view(),name='product_detail'),
]