from django.urls import path

from .views import (HomePageView)

app_name = 'pages'

#<converter:data >

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]