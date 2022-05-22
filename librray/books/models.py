from imp import release_lock
from venv import create
from django.db import models
from uuid import uuid4
# Create your models here.

class Books(models.Model):
    id_books = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    release_year=models.IntegerField()
    status = models.CharField(max_length=50)
    pages = models.IntegerField()
    publishig_company = models.CharField(max_length=255)
    create_at=models.DateTimeField(auto_now_add=True)
    
    
