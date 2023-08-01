from django.db import models
from django.contrib.auth.models import AbstractUser, User

# class User(AbstractUser):
#     name = models.CharField(max_length=255)
#     email = models.CharField(max_length=255, unique=True)
#     password = models.CharField(max_length=255)
#     username = None
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []


class Counter(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, default='none')
    value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.name

    def verify(self, newValue: float) -> bool:
        # Your verification logic here
        return newValue >= 0
    
class Image(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.URLField()
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.url

    
class Report(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.URLField()
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self) :
        return self.url

