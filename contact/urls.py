from django.urls import path
from .views import ContactFromView


app_name = 'contact'

#<converter:data >

urlpatterns = [
    path('',ContactFromView.as_view(),name='contact'),
   
]