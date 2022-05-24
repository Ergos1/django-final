from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models import *
from api.serializers import *


class Books(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializers = BookSerializer(books, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

