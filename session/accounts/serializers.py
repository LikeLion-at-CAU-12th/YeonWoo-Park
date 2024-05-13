from rest_framework_simplejwt.serializers import RefreshToken
from rest_framework import serializers
from .models import User

# 회원가입 구현
class RegisterSerializer(serializers.ModelSerializer): # ModelSerializer를 상속받음
    password = serializers.CharField(required=True) # serializer를 통해 패스워드가 맞는지 확인
    username = serializers.CharField(required=True)
    email = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['password', 'username', 'email'] # 위에 적은 필드는 아래에도 꼭 적어줘야 함
    
    def save(self, request):
        user = User.objects.create(
            username=self.validated_data['username'], # 검증된 데이터 중 username이라는 키 값을 가진 값을 가져옴
            email=self.validated_data['email'],
        )
        
        # password 암호화
        user.set_password(self.validated_data['password']) # set_password로 암호화
        user.save()

        return user
    
    def validate(self, data): # 중복 email로 가입하는 것을 방지하기 위해 검증하는 메서드
        # email = data["email"] # 이는 email에 해당하는 값이 없으면 키에러가 뜸. 따라서 아래처럼 써주는 것
        email = data.get('email', None)
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('email already exists')
        
        return data

class AuthSerializer(serializers.ModelSerializer): # 로그인/로그아웃 구현
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'password']
    
    def validate(self, data): # DB에 회원 정보가 존재하는지, 그리고 저장된 비밀번호와 사용자 입력값이 일치하는지 검증
        username = data.get("username", None)
        password = data.get("password", None)
        
        user = User.get_user_or_none_by_username(username=username)
        
        if user is None: # 찾는 유저가 없는 경우
            raise serializers.ValidationError("user account not exist")
        else:
            if not user.check_password(raw_password=password): # 패스워드가 틀린 경우
                raise serializers.ValidationError("wrong password")
        
        token = RefreshToken.for_user(user)
        refresh_token = str(token)
        access_token = str(token.access_token)
        
        data = {
            "user": user,
            "refresh_token": refresh_token,
            "access_token": access_token,
        }
        
        return data
        