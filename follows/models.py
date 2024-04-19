from django.db import models
from django.contrib.auth.models import User

class Follow(models.Model):
  follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
  followed_user = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)

class Meta:
  unique_together = ('follower', 'followed_user')

def __str__(self):
  return f'{self.follower} follows {self.followed_user}'
