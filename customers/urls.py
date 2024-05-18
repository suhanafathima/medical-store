from django.contrib import admin
from django.urls import path,include
from customers  import views
urlpatterns = [
   path('login/',views.login_page,name='login'),
   path('signup/',views.signup,name='signup'),
   # path('products',include('products.urls'))
]