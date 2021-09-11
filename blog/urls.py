from django.urls import path
from django.contrib import admin
from .views import *

urlpatterns = [
    path('', main_view, name='main_url'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('tags/', tags_list, name='tags_list_url'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url')
]
