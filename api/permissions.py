# api/permissions.py

from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only the owner of a book to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request, so we'll always allow GET, HEAD, or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the user who added the book.
        return obj.added_by == request.user


class IsLibrarianOrAdmin(permissions.BasePermission):
    """
    Custom permission to only allow librarians or admin users to add books.
    """

    def has_permission(self, request, view):
        # Allow access if the user is authenticated and is an admin or librarian
        return request.user.is_authenticated and (request.user.is_staff or request.user.groups.filter(name='librarians').exists())


