from django.shortcuts import render
from django.http import JsonResponse # 추가 
from django.shortcuts import get_object_or_404 # 추가

# Create your views here.

def hello_world(request):
    if request.method == "GET":
        return JsonResponse({
            'status' : 200,
            'data' : "Hello lielion-12th!"
        })
    
def index(request):
    return render(request, 'index.html')

def work_standard(request):
    if request.method == "GET":
        return JsonResponse({
            'status' : 200,
            'success' : True,
            'message' : '메시지 전달 성공!',
            'data' : [
                {
                    "name" : "박연우",
                    "age" : 22,
                    "major" : "소프트웨어학부"
                },
                {
                    "name" : "김예찬",
                    "age" : 25,
                    "major" : "소프트웨어학부"
                }
            ]
        })

def work_challenge(request):
    Me = {'name':'박연우', 'age':'22', 'dept':'CSE', 'github':'https://github.com/only4wxx'}
    Reviewer = {'name':'김예찬', 'age':'25', 'dept':'CSE', 'github':'https://github.com/Yeahcold'}
    return render(request, 'page.html', {'Me': Me, 'Reviewer': Reviewer})

from django.views.decorators.http import require_http_methods
from posts.models import *
import json
from datetime import *

@require_http_methods(["GET"])
def post_list(request): # 전체 post를 읽어옴
    if request.method == "GET":
        post_all = Post.objects.all()

        # 각 데이터를 Json 형식으로 반환하여 리스트에 저장
        post_json_all = []
        
        for post in post_all:
            post_json = {
                "id": post.id,
                "title" : post.title,
                # "writer": post.writer,
                "category": post.category
            }
            post_json_all.append(post_json)

        return JsonResponse({
            'status': 200,
            'message': '게시글 목록 조회 성공',
            'data': post_json_all
        })

@require_http_methods(["GET"])
def get_post_detail(request,id): # 개별 post를 읽어옴
    post = get_object_or_404(Post, pk=id)
    post_detail_json = {
        "id" : post.id,
        "title" : post.title,
        "content" : post.content,
        # "writer" : post.writer, # Post 테이블의 writer가 User 테이블을 참조하는 외래키라서 그런지 이 코드가 작동하지 않음... 따라서 주석처리
        "category" : post.category,
    }

    return JsonResponse({
        'status' : 200,
        'message' : '게시글 조회 성공',
        'data' : post_detail_json
    })

@require_http_methods(["GET"])
def get_comments_of_post(request, id): # 특정 게시글에 포함된 모든 comment 읽어오는 API 만들기
    if request.method == "GET":
        post = get_object_or_404(Post, pk=id)
        comment_all = Comment.objects.filter(post_id=post.id)

        comment_json_all = []

        for comment in comment_all:
            comment_json = {
                "id": comment.id,
                # "writer": comment.writer,
                "content" : comment.content
            }
            comment_json_all.append(comment_json)
        
        return JsonResponse({
            'status': 200,
            'message': '게시글에 포함된 모든 comment 조회 성공',
            'data': comment_json_all
        })

@require_http_methods(["GET"])
def a_week_post_list(request):
    if request.method == "GET":
        post_all = Post.objects.filter(created_at__range=(date(2024, 4, 4), date(2024, 4, 10))).order_by('-created_at')

        post_json_all = []
        
        for post in post_all:
            post_json = {
                "id": post.id,
                "title" : post.title,
                # "writer": post.writer,
                "category": post.category
            }
            post_json_all.append(post_json)

        return JsonResponse({
            'status': 200,
            'message': '게시글 목록 조회 성공',
            'data': post_json_all
        })