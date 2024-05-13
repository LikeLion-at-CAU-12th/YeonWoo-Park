from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    조회(GET)는 인증된 유저 모두에게 허용한다.
    수정(PUT) 및 삭제(DELETE)는 작성자에 한하여 허용한다.
    """
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: # 요청된 메소드가 안전한 메소드인 경우 허용
            return True
        return obj.writer.id == request.user.id # 작성자인지 확인

class IsSecretKey(permissions.BasePermission):
    """
    header에 key 값을 입력 받은 후 key 문구를 맞게 입력한 사용자만 모든 API 요청을 허용
    """

    def has_permission(self, request, view):
        return request.headers.get('SecretKey') == '0921'