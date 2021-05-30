from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length =200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = 'Categories'

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    category = models.ForeignKey(Category, related_name='categories', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']

