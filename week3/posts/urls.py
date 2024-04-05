from django.urls import path
from posts.views import *

urlpatterns = [
    # path('', hello_world, name = 'hello_world'),
    path('introduction', work_standard, name="introduction"),
    path('page', work_challenge, name="page"),
    path('', post_list, name="post_list"), # Post 전체 조회
    path('week', a_week_post_list, name="최근 일주일 동안 작성된 게시글 목록 조회"),
    path('<int:id>', get_post_detail, name = "게시글 조회"),
    path('<int:id>/comment', get_comments_of_post, name = "게시글의 모든 코멘트 조회")
]