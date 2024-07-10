from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('blogs/', views.blogs, name='blogs'),
    path('categories/', views.categories, name='categories'),
    path('users/', views.users, name='users'),
    path('blogs/blogdetails/<int:id>', views.blogdetails, name='blogdetails'),
    path('blogs/blogdetails/<int:id>/comments/', views.comments, name='comments'),
]

