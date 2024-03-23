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