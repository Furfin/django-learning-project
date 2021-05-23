from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentCreateView, com_delete

urlpatterns = [
  path('',PostListView.as_view(), name='blog-home'),
  path('<int:pk>',PostListView.as_view(), name='blog-home'),
  path('post/new/',PostCreateView.as_view(), name='post-create'),
  path('post/<int:pk>/',PostDetailView.as_view(), name='post-detail'),
  path('post/<int:pk>/update',PostUpdateView.as_view(), name='post-update'),
  path('post/<int:pk>/delete',PostDeleteView.as_view(), name='post-delete'),
  path('post/<int:pk>/ccomment',CommentCreateView.as_view(), name='post-comment'),
  path('com/<int:pk>/delete',com_delete, name='com-delete'),
  path('about/',views.about, name='blog-about'),
]