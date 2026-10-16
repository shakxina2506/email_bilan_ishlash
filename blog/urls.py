from django.urls import path

from .views import PostListView,PostDetailView,PostCreateView,PostDeleteView,PostUpdateView

urlpatterns = [
    path('',PostListView.as_view(),name='post_list'),
    path('detail/<int:pk>/',PostDetailView.as_view(),name='post_detail'),
    path('create/',PostCreateView.as_view(),name='post_create'),
    path('delete/<int:pk>/',PostDeleteView.as_view(),name='post_delete'),
    path('update/<int:pk>/',PostUpdateView.as_view(),name='post_update'),
]