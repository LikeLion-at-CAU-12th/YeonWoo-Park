###Model Serializer case
from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
		# 어떤 모델을 시리얼라이즈할 건지
        model = Post
		# 모델에서 어떤 필드를 가져올지
		# 전부 가져오고 싶을 때
        fields = "__all__"
        # fields = ['id', 'title', 'content', 'image', 'writer', 'category', 'created_at', 'updated_at']
    
    def create(self, validated_data): # serializer를 대상으로 save() 메소드를 호출하여 DB 인스턴스를 생성할 때의 동작 정의
        print('11111111111111111')
        instance = Post.objects.create(**validated_data)
        print('222222222222222222222222222')
        print(instance.thumbnail)
        image = validated_data.get("thumbnail", None)
        ext = str(image).split('.')[-1] # ext에 확장자 명이 담김
        ext = ext.lower() # 확장자를 소문자로 통일
        if ext == 'png': # png 파일이 입력으로 들어온 경우에 에러 발생
            raise serializers.ValidationError(".png file is not allowed")
        
        return instance


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"