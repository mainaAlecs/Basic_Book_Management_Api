# books/serializers.py
from rest_framework import serializers
from .models import Book


# Serializer for the Book Model.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'availability']
