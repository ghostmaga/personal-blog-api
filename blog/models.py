from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
     name = models.CharField(max_length=255, unique=True)
     description = models.TextField(blank=True)

     def __str__(self):
          return self.name
     
class BlogPost(models.Model):
     title = models.CharField(max_length=255)
     content = models.TextField()
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     author = models.ForeignKey(User, on_delete=models.CASCADE)
     category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

     def __str__(self):
          return self.title   
     
class Comment(models.Model):
     post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     content = models.TextField()
     created_at = models.DateTimeField(auto_now_add=True)

     def __str__(self):
          return f'{self.user.username} commented on {self.post.title}'