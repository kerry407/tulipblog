from django.urls import path 
from django.conf import settings
from . import views 
from .views import PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('blog-detail/<int:pk>/', views.blog, name='blog-detail'),
    path('create_post/', PostCreateView.as_view(), name='create-post'),
    path('blog-detail/<int:pk>/update/', PostUpdateView.as_view(), name='update-post'),
    path('blog-detail/<int:pk>/delete/', PostDeleteView.as_view(), name='delete-post'),
    path('category/<str:cats>/', views.category, name='category'),
    path('contact/', views.contact, name='blog-contact'),
]


