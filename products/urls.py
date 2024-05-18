from . import views
from django.urls import path

urlpatterns = [
        path('',views.greeting2,name='home2'),
        path('create/',views.product_create,name='createproduct'),
        path('view/',views.product_read,name='viewproduct'),
       path('update/<int:id>/',views.product_update,name='updateproduct'),
       path('delete/<int:pk>',views.product_delete,name='deleteproduct'),
        path('listing/',views.listing,name='page_list'),
        path('search/',views. search_medicine, name='search_medicine'),
        path('logout/', views.logout_view,name='logout')
    ]