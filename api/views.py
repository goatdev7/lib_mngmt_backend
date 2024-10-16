from django.shortcuts import render
from rest_framework import generics, permissions, filters
from .models import Book
from .serializers import BookSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated

# Create your views here.

# List all books and create a new book
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author', 'isbn']  # Enable searching by these fields
    ordering_fields = ['published_date', 'title']  # Enable ordering by these fields

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class UserBooksListView(generics.ListAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Return books that were added by the current user
        user = self.request.user

        title = self.request.query_params.get('title', None)
        author = self.request.query_params.get('author', None)
        description = self.request.query_params.get('description', None)

        queryset = Book.objects.filter(added_by = self.request.user)

        if title:
            queryset = queryset.filter(title__icontains = title)
        elif author:
            queryset = queryset.filter(author__icontains = author)
        elif description:
            queryset = queryset.filter(description__icontains = description)

        return queryset