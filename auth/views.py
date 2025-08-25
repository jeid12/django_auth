from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer

@api_view(["POST"])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({"user": UserSerializer(user).data}, status=201)
    return Response(serializer.errors, status=400)
