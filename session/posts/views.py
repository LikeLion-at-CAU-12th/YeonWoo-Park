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

@require_http_methods(["POST", "GET"])
def post_list(request):
    if request.method == "POST":
        new_post = Post()

        new_post.title = request.POST['title']
        new_post.content = request.POST.get('content')
        new_post.image = request.FILES.get('image')
        writer_id = request.POST.get('writer')
        new_post.writer = User.objects.get(pk=writer_id)
        new_post.category = request.POST.get('category')
        new_post.save()

        return JsonResponse({
            'status': 200,
            'message': '게시글 생성 성공',
            'data': {
                "id": new_post.id,
                "title" : new_post.title,
                "content": new_post.content,
                "image_url": new_post.image.url if new_post.image else "",
                "writer": new_post.writer.id,
                "category": new_post.category
            },

        })

    if request.method == "GET":
        post_all = Post.objects.all()

        # 각 데이터를 Json 형식으로 반환하여 리스트에 저장
        post_json_all = []
        
        for post in post_all:
            post_json = {
                "id": post.id,
                "title" : post.title,
                "content": post.content,
                "image_url": post.image.url if post.image else "",
                "writer": post.writer.id,
                "category": post.category
            }
            post_json_all.append(post_json)

        return JsonResponse({
            'status': 200,
            'message': '게시글 목록 조회 성공',
            'data': post_json_all
        })

@require_http_methods(["GET", "PATCH", "DELETE"])
def post_detail(request,id):
    if request.method == "GET":
        post = get_object_or_404(Post, pk=id)

        post_detail_json = {
            "id" : post.id,
            "title" : post.title,
            "content" : post.content,
            "image_url": post.image.url if post.image else "",
            "writer" : post.writer.id,
            "category" : post.category,
        }

        return JsonResponse({
            'status' : 200,
            'message' : '게시글 조회 성공',
            'data' : post_detail_json
        })
    
    if request.method == "PATCH":
        body = json.loads(request.body.decode('utf-8'))

        update_post = get_object_or_404(Post, pk=id)

        update_post.title = body['title']
        update_post.content = body['content']
        update_post.category = body['category']

        update_post.save()

        update_post_json = {
            "id": update_post.id,
            "title" : update_post.title,
            "content": update_post.content,
            "image_url": update_post.image.url if update_post.image else "",
            "writer": update_post.writer.id,
            "category": update_post.category,
        }

        return JsonResponse({
            'status': 200,
            'message': '게시글 수정 성공',
            'data': update_post_json
        })
    
    if request.method == "DELETE":
        delete_post = get_object_or_404(Post, pk=id)
        delete_post.delete()

        return JsonResponse({
                'status': 200,
                'message': '게시글 삭제 성공',
                'data': None
        })

@require_http_methods(["GET"])
def get_comments_of_post(request, id): # 특정 게시글에 포함된 모든 comment 읽어오는 API 만들기
    if request.method == "GET":
        comment_all = Comment.objects.filter(post_id=id)

        comment_json_all = []

        for comment in comment_all:
            comment_json = {
                "id": comment.id,
                "writer": comment.writer.id,
                "content" : comment.content
            }
            comment_json_all.append(comment_json)
        
        return JsonResponse({
            'status': 200,
            'message': '게시글에 포함된 모든 comment 조회 성공',
            'data': comment_json_all
        })

@require_http_methods(["GET"])
def a_week_post_list(request): # 최근 일주일 동안 작성된 게시글 목록을 볼 수 있는 API
    if request.method == "GET":
        post_all = Post.objects.filter(created_at__gte=(date.today() - timedelta(days=6))).order_by('-created_at')

        post_json_all = []
        
        for post in post_all:
            post_json = {
                "id": post.id,
                "title" : post.title,
                "writer": post.writer.id,
                "category": post.category
            }
            post_json_all.append(post_json)

        return JsonResponse({
            'status': 200,
            'message': '게시글 목록 조회 성공',
            'data': post_json_all
        })