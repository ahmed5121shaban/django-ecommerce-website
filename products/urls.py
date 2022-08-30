from django.urls import path
from .views import ProductsList,ProcuctDetail,BrandList,BrandDetail,CategoryList

app_name = 'products'

urlpatterns = [
    path('', ProductsList.as_view(),name='product_list'),
    path('<int:pk>', ProcuctDetail.as_view(),name='product_detail'),
    path('brand/', BrandList.as_view(),name='brand_list'),
    path('brand/<int:pk>', BrandDetail.as_view(),name='brand_detail'),
    path('category/', CategoryList.as_view(),name='category_list'),
]