from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('article/new/', views.article_create, name='article_create'),
    path('category/<int:category_id>/', views.articles_by_category, name='articles_by_category'),
    path('category/new/', views.category_create, name='category_create'),
]
