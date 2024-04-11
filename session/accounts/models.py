from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser): # 정의하고자 했던 내용이 모두 있는 AbstractUser 모델 사용
    pass #해당 세션에서 바로 유저모델을 사용할 것은 아니기 때문에 pass로 넣겠습니다.