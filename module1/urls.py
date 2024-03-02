from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('hello/', hello, name='hello'),
    path('', NewHomePage, name='NewHomePage'),
    path('Travel/', Travel, name='Travel'),
    path('print_to_console/', print_to_console, name='print_to_console'),
    path('p/', print1, name='print'),
    path('otp/', randomcall1, name="randomcall1"),
    path('otplogic/', randomcall, name="randomcall"),
    path('get_date/', get_date, name='get_date'),
    path('get_date1/', get_date1, name='get_date1'),
    path('register/',registerlogin,name='registerlogin'),
    path('registerlogin/',registerloginfunction,name='registerloginfunction'),
    path('Pie/',pie_chart,name='Pie'),
    path('piechart/',piechart,name='piechart'),
    path('car/',car_rent,name='car'),
    path('weatherpagecall/',weatherpagecall,name='weatherpagecall'),
    path('weather/',weatherlogic,name='weatherlogic'),

    path('login/',login,name='login'),
    path('signup/',signup,name='signup'),
    path('login1/',login1,name='login1'),
    path('signup1/',signup1,name='signup1'),
    path('logout/',logout,name='logout'),
]
