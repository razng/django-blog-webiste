from django.urls import path
from . views import PostList, PostDetail, AddPost

urlpatterns = [
    path('',PostList.as_view(), name='index'),
    path('<slug:slug>',PostDetail.as_view(), name='post_detail'),
    path('add-post/',AddPost.as_view(), name='add_post')
]
