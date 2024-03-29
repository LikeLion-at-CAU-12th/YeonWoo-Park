from django.urls import path
from posts.views import *

urlpatterns = [
    path('', hello_world, name = 'hello_world'),
    path('introduction', work_standard, name="introduction"),
    path('page', work_challenge, name="page"),
    path('<int:id>', get_post_detail, name = "게시글 조회"),
]