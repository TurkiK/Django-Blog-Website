from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('blogs/', views.blogs, name='blogs'),
    path('blogs/blogdetails/<int:id>', views.blogdetails, name='blogdetails'),
]

