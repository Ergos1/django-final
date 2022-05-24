from rest_framework.decorators import api_view, permission_classes

from api.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.contrib.auth.models import User

import logging
logger = logging.getLogger('django')


@api_view(["GET"])
@permission_classes([AllowAny])
def list_user(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
