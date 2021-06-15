from django.urls import path

from .views import (ArticleDetailView,ArticleListView,GenreListView, ArticleCreateView,ArticleUpdateView)

app_name = 'articles'
#<converter:data >

urlpatterns = [
    path('',ArticleListView.as_view(),name='article_list'),
    path('<slug:slug>/', ArticleDetailView.as_view(), name='article_detail'),
    path('articles/genre/<str:genre>/',GenreListView.as_view(),name='genre_list'),
    path('add/',ArticleCreateView.as_view(),name='add_article'),
    path('<slug:slug>/edit',ArticleUpdateView.as_view(),name='edit_article'),

]