from django.urls import path

from .views import (HomePageView,ServicesPageView)

app_name = 'pages'

#<converter:data >

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('services',ServicesPageView.as_view(),name='services')
]