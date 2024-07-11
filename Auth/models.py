from django.db import models
from django.conf import settings


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    custom_id = models.IntegerField(unique=True, null=True, blank=True)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)
    # Additional fields can be added here

    def __str__(self):
        return self.user.username


