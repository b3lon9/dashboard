# checking SQL tabular
# python manage.py sqlmigrate

from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=10)
    user_pw = models.CharField(max_length=20)
    publish = models.DateTimeField() # timezone.now()

    def __str(self):
        return self.user_id