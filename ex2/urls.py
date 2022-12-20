from django.contrib.auth.views import LoginView
from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('product_list', ProductList.as_view(), name='product_list'),
    path('about_us', AboutUs.as_view(), name='about_us'),
    path('contact', Contact.as_view(), name='contact'),
    path('login', LoginView.as_view(), name='login'),
    path('create', Create.as_view(), name='create'),
]