from django.contrib import admin
from django.urls import path
from App_Services import views
from django.conf.urls import include,url

urlpatterns = [
     url('login/', views.getloginview.as_view()),
    #  url('autlogin/', views.loginview),
    # url(r'^$',views.getloginview.as_view(), name='login'),
    
]