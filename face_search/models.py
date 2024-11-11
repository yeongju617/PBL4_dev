# face_search/models.py
from django.db import models
from accounts.models import User

class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_path = models.CharField(max_length=255)
    upload_time = models.DateTimeField(auto_now_add=True)

class PhotoStatus(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    photo_order = models.IntegerField()
    STATUS_CHOICES = [
        ('reject', 'Reject'),
        ('success', 'Success')
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='reject')
