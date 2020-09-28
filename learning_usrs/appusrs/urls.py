from django.conf.urls import url
from appusrs import views
from django.urls import path,include

#TEMPLATE URLS
app_name='appusrs'

urlpatterns=[
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login')

]