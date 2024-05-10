from django.shortcuts import render

# Create your views here.
from rest_framework_simplejwt.serializers import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from accounts.serializers import *

class RegisterView(APIView):

    def post(self, request): # 회원가입을 수행
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True): # is_valid()로 유효성 검사
            user = serializer.save(request)
            token = RefreshToken.for_user(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "user": serializer.data,
                    "message": "register success",
                    "token": {
                        "access_token": access_token,
                        "refresh_token": refresh_token,
                    },
                },
                status=status.HTTP_201_CREATED,
            )
            return res
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AuthView(APIView):
    def post(self, request): # 로그인을 수행
        serializer = AuthSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data["user"]
            access_token = serializer.validated_data["access_token"]
            refresh_token = serializer.validated_data["refresh_token"]
            res = Response(
                {
                    "user": {
                        "id": user.id,
                        "email": user.email,
                    },
                    "message": "login success",
                    "token": {
                        "access_token": access_token,
                        "refresh_token": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )
            res.set_cookie("access-token", access_token, httponly=True) # set_cookie를 통해 발행한 토큰 정보가 'Cookie'라는 key의 value로 저장됨
            res.set_cookie("refresh-token", refresh_token, httponly=True)
            return res
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)