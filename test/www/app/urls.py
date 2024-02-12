from django.urls import path
from .views import *

urlpatterns = [
    # path('',PostTemp.as_view(),name='index'),
    path('',index,name='home'),
    path('check/<int:pk>',check,name='check'),
    path('delete/<int:pk>',delete,name='delete'),
    path('add/',add,name='add'),
    path('edit/<int:pk>',edit,name='edit'),
    path('info/<int:pk>',info,name='info'),
]
