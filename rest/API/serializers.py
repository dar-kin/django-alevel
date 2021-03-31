from rest_framework import serializers
from rest.models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["name", "age"]


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["name", "author"]


class AuthorWithBooksSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["name", "age", "books"]