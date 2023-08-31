from django.urls import path
from .views import Blog_list

urlpatterns = [
    path('blog/', Blog_list, name='blog_list'),
]