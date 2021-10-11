from os import name
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name="blog-about"),
    path('create/', views.createPost_view, name='createPost'),
    path('detail-view/<int:pk>', views.postDetail_view, name='detail-view'),
    path('update-view/<int:pk>', views.postUpdate_view, name='update-view'),
    path('delete-view/<int:pk>', views.postDelete_view, name='delete-view'),
]
