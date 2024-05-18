from django.contrib import admin
from django.urls import path,include
from customers  import views
urlpatterns = [
    path('',views.greeting,name='home'),
    path('customers/',include('customers.urls')),
    path('products/',include('products.urls')),
    path('productapi/', include('productapi.urls')),
    path('login/',views.login_page,name='login'),
    path('signup/',views.signup,name='signup'),
   
]