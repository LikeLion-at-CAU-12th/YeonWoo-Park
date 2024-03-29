from django.db import models

# Create your models here.

## 추상 클래스 정의
class BaseModel(models.Model): # models.Model을 상속 받음
    created_at = models.DateTimeField(verbose_name="작성일시", auto_now_add=True)
    updated_at = models.DateTimeField(verbode_name="수정일시", auto_now=True)
    
    class Meta:
        abstract = True

## 정의한 추상 클래스를 클래스에서 상속 받음
class Post(BaseModel):

    CHOICES = (
        ('DIARY', '일기')
        ('STUDY', '공부')
        ('ETC', '기타')
    )

    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name="제목", max_length=20)
    content = models.TextField(verbose_name="내용")
    writer = models.CharField(verbose_name="작성자", max_length=10)
    category = models.CharField(choices=CHOICES, max_length=20)