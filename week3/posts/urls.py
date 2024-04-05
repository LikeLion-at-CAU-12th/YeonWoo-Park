from django.urls import path
from posts.views import *

urlpatterns = [
    # path('', hello_world, name = 'hello_world'),
    path('introduction', work_standard, name="introduction"),
    path('page', work_challenge, name="page"),
    path('', post_list, name="post_list"), # Post 전체 조회
    path('<int:id>', get_post_detail, name = "게시글 조회"),
    path('<int:id>/comment', get_comments_of_post, name = "게시글의 모든 코멘트 조회")
]