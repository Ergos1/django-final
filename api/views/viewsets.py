from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny 
from django.contrib.auth import login, logout, authenticate
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


from api.models import *
from api.permissions import IsAdmin
from api.serializers import *

class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes=[AllowAny]

    @action(methods=['post'], detail=False)
    def register(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User was created"}, status=status.HTTP_201_CREATED)

        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class BookViewSet(viewsets.ViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdmin]

    def list(self, request):
        books = Book.objects.all()
        serializers = BookSerializer(books, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book, many=False)

        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(instance=book, data=request.data, many=False, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(instance=book, data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        book = Book.objects.get(pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class JournalViewSet(viewsets.ViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    permission_classes = []

    def list(self, request):
        journals = Journal.objects.all()
        serializers = JournalSerializer(journals, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = JournalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        book = Journal.objects.get(pk=pk)
        serializer = JournalSerializer(book, many=False)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        book = Journal.objects.get(pk=pk)
        serializer = JournalSerializer(instance=book, data=request.data, many=False, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        book = Journal.objects.get(pk=pk)
        serializer = JournalSerializer(instance=book, data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        book = Journal.objects.get(pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)