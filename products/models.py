from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=50)
  content = models.TextField()
  price = models.IntegerField()
  views = models.IntegerField(default=0)
  jjims = models.IntegerField(default=0)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)