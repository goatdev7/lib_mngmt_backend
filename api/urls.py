from django.urls import path, include
from .views import BookListCreateView, BookDetailView, UserBooksListView

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),  # Login, logout
    path('auth/registration/', include('dj_rest_auth.registration.urls')),  # Registration
    path('books/', BookListCreateView.as_view(), name='book-list'), 
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('my-books/', UserBooksListView.as_view(), name='user-books'),  # New route
]