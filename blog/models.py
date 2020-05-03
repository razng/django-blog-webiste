from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

STATUS=(
    (0, "Draft"),
    (1, "Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_on"]

    def get_absolute_url(self):
        return reverse('index')
    