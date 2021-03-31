from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import BookSerializer, AuthorSerializer, AuthorWithBooksSerializer
from rest.models import Book, Author


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    @action(detail=True, methods=["get"])
    def author_with_books(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        return Response(AuthorWithBooksSerializer(author).data)

    def get_queryset(self):
        search = self.request.query_params.get("book_name", False)
        queryset = super().get_queryset()
        if search:
            books = Book.objects.filter(name__contains=search).values_list("author")
            queryset = Author.objects.filter(id__in=books)
        return queryset


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        serializer.save(name=serializer.validated_data.get('name') + "!")

    def get_queryset(self):
        age = self.request.query_params.get("author_age", False)
        queryset = super().get_queryset()
        if age and isinstance(int(age), int):
            queryset = queryset.filter(author__age__gte=age)
        return queryset
