from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 255)
    author = models.CharField(max_length = 255)
    description = models.TextField(blank = True)
    isbn = models.CharField(max_length = 13, unique = True)
    pub_date = models.DateField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books_added')


    def __str__(self):
        return self.title
