from django.db import models
from accounts.models import User

# Create your models here.

## 추상 클래스 정의
class BaseModel(models.Model): # models.Model을 상속 받음
    created_at = models.DateTimeField(verbose_name="작성일시", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="수정일시", auto_now=True)
    
    class Meta:
        abstract = True

## 정의한 추상 클래스를 클래스에서 상속 받음
class Post(BaseModel):

    CHOICES = (
        ('DIARY', '일기'),
        ('STUDY', '공부'),
        ('ETC', '기타')
    )

    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name="제목", max_length=50)
    content = models.TextField(verbose_name="내용")
    image = models.ImageField(upload_to="images/", blank=True, null=True, verbose_name="이미지")
    writer = models.ForeignKey(User, on_delete=models.CASCADE, db_column="writer", verbose_name="작성자")
    category = models.CharField(choices=CHOICES, max_length=30)
    thumbnail = models.URLField(null=True, max_length=200)

class Comment(BaseModel):

    id = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, db_column="post_id", verbose_name="코멘트를 작성할 게시글")
    content = models.TextField(verbose_name="내용")
    writer = models.ForeignKey(User, on_delete=models.CASCADE, db_column="writer", verbose_name="작성자")