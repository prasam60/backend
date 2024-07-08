from django.db import models

# Create your models here.

class Member(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    email = models.CharField(max_length=100, blank=False, null=False)
    phone = models.CharField(max_length=20, blank=False, null=False)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return str(self.first_name + ' ' + self.last_name)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)