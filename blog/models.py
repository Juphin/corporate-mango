import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.utils import timezone


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=200, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Article(models.Model):
    title = models.CharField(max_length=200, null=False)
    slug = models.SlugField()
    content = models.TextField()
    state = models.BooleanField(null=False, default=True)
    pub_date = models.DateTimeField(default=timezone.now, verbose_name='pub_date')
    #pub_time = models.TimeField(default=datetime., verbose_name='pub_time')

    class Meta:
        verbose_name = "article"
        ordering = ['pub_date']

    def __str__(self):
        return self.title
