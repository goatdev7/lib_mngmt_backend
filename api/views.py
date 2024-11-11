from django.shortcuts import render
from rest_framework import generics, permissions, filters
from .models import Book
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BookSerializer
from .permissions import IsOwnerOrReadOnly, IsLibrarianOrAdmin
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q


# List all books and create a new book
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class UserBooksListView(generics.ListAPIView):
    serializer_class = BookSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # queryset = Book.objects.filter(added_by = self.request.user)
        queryset = Book.objects.all()
        search = self.request.query_params.get('search', None)

        # # If a search term is provided, filter across title, author, and description
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(author__icontains=search) |
                Q(description__icontains=search)
            )

        return queryset

# class UserAddBooksView(generics.Lis)
class UserRoleView(APIView):
    permission_classes = [IsLibrarianOrAdmin]

    def get(self, request):
        user = request.user
        return Response({
            "is_staff": user.is_staff,
            "groups": [group.name for group in user.groups.all()],
        })