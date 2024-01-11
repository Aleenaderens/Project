from django.urls import path
from .views import *

urlpatterns = [
    path('',IndexView.as_view(),name='Homepage'),
    path('login/',loginPage,name='login'),
    path('signup/',signlogin,name='usersigning'),
    path('usersignup/',signup,name='signing'),
    path('details/',details,name='details'),
    path('about/',aboutpage,name='about'),
    path('ethnic_wears/',ethnicpage,name='ethnicpage'),
    path('Western_wears/',westernpage,name='westernpage'),
    path('casual_wears/',casualpage,name='casualpage'),
    path('contact/',contactpage,name='contact'),
    path('addtocart/',addtocart),
    path('placeorder/',placeorder,name='placeholder'),
    path('<str:name>',CategoryView.as_view(),name='western'),
]
