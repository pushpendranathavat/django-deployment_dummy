from django.urls import path
from apptemplates import views
#Template tagging
app_name = 'apptemplates'

urlpatterns=[
        path('relative/', views.relative, name='relative'),
        path('other/', views.other, name='other'),
        path('index/', views.index, name='index')
]