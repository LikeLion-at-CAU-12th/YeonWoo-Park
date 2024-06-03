from rest_framework_simplejwt.serializers import RefreshToken
from rest_framework import serializers
from .models import User
from allauth.socialaccount.models import SocialAccount

class OAuthSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ["email"]

    def validate(self, data):
        email = data.get("email", None)
        
        user = User.get_user_or_none_by_email(email=email)
        
        if user is None:
            raise serializers.ValidationError("user account not exists")
        
        social_user = SocialAccount.objects.get(user=user)  # 소셜로그인 계정 유무 확인
        if social_user.provider != 'google':
	        raise serializers.ValidationError("user did not sign up with a social account")
        
        token = RefreshToken.for_user(user)
        refresh_token = str(token)
        access_token = str(token.access_token)

        data = {
            "user": user,
            "refresh_token": refresh_token,
            "access_token": access_token,
        }

        return data