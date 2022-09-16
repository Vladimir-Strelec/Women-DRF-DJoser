from django.contrib.auth.models import User
from django.db import models


class WomanModel(models.Model):
    name = models.CharField(max_length=100,)
    context = models.CharField(max_length=300,)
    create_profile = models.DateTimeField(auto_now_add=True,)
    update_profile = models.DateTimeField(auto_now=True,)
    user = models.ForeignKey(User, verbose_name='profile', on_delete=models.CASCADE)
