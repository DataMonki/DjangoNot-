from django.urls import path

from .views import (HomePageView, ArticleDetailView,ArticleListView,GenreListView)

app_name = 'articles'

#<converter:data >

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),
    path('articles/',ArticleListView.as_view(),name='article-list'),
    path('articles/genre/<str:genre>/',GenreListView.as_view(),name='genre-list')

]