 
from django.urls import path
from . import views
 

urlpatterns = [
    path('', views.showAllProduct, name='showProducts'),
    path('product/<int:pk>', views.productDetail, name="product"),
    path('addproduct', views.addProduct, name="addproduct"),
    path('updateproduct/<int:pk>', views.updateProduct, name="updateproduct"),
    path('deleteproduct/<int:pk>', views.deleteProduct, name="deleteproduct"),
] 
