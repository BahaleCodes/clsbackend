from djongo import models
from django.contrib.auth.models import User

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    fileName = models.CharField(max_length=32, null=True)
    fileType = models.CharField(max_length=32, null=True)
    location = models.CharField(max_length=32, null=True)
    table = models.CharField(max_length=32, null=True)
    field = models.CharField(max_length=32, null=True)
    category = models.CharField(max_length=32, null=True)

