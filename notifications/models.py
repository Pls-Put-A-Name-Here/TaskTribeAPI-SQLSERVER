from django.db import models
from django.utils import timezone
from Core.User.models import User

# Create your models here.
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    type = models.CharField(max_length=20, choices=[
        ('INFO', 'Info'),
        ('WARNING', 'Warning'),
        ('ERROR', 'Error')
    ], default='INFO')
    date_created = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)
    

    def __str__(self):
        return self.title