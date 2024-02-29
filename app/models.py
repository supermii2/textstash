from django.db import models

# Create your models here.
class Text(models.Model):
    title = models.CharField(50, unique=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)