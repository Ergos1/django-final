from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework.fields import SerializerMethodField

from api.models import Book, Journal


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    role = SerializerMethodField(method_name="get_role", read_only=True)

    def validate_password(self, value: str) -> str:
        return make_password(value)

    def get_role(self, instance):
        user = instance
        if user.is_staff == True:
            return "SuperAdmin"
        return "Guest"
        
    class Meta:
        model = User
        fields = ('id', 'password', 'username', 'is_staff', 'role')


class BookSerializer(serializers.ModelSerializer):
    genre_name = SerializerMethodField(method_name="get_genre_name", read_only=True)

    def get_genre_name(self, instance):
        return instance.get_genre_display()

    class Meta:
        model = Book
        fields = "__all__"

class JournalSerializer(serializers.ModelSerializer):
    publisher = UserSerializer(read_only=True)
    publisher_id = serializers.IntegerField(write_only=True)
    type_name = SerializerMethodField(method_name="get_type_name", read_only=True)

    def get_type_name(self, instance):
        return instance.get_type_display()

    class Meta:
        model = Journal
        fields = "__all__"