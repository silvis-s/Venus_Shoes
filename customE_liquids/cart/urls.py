from django.urls import path
from . import views
app_name = "cart"

urlpatterns = [
    path('add/<int:product_id>/', views.addProd, name="add"),
    path('delete/<int:product_id>/', views.deleteProd, name="delete"),
    path('minus/<int:product_id>/', views.minusProd, name="minus"),
    path('clean/', views.cleanProd, name="clean"),

]
