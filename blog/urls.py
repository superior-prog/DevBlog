from django.urls import path
from .views import *

urlpatterns = [
    # blog urls
    path('', blog_home_view, name='blog-home'),
    path('blogs/<str:pk>/', blogs_view, name='blogs'),
    path('post/<str:slug>/', blog_details_view, name='blog-details'),
    path('add-blog', add_blog_view, name='add-blog'),
    path('edit-blog/<str:slug>/', edit_blog_view, name='edit-blog'),
    path('delete-blog/<str:slug>/', delete_blog_view, name='delete-blog'),
    path('edit-comment/<str:pk>/', edit_comment_view, name='edit-comment'),
    path('delete-comment/<str:pk>/', delete_comment_view, name='delete-comment'),
]

