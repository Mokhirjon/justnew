from django.urls import path
from .views import index,get_all
urlpatterns=[path('get_all/',get_all),
    path('index/',index)
]