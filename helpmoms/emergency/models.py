from django.conf import settings
from django.db import models
from django.utils import timezone

class Emergency(models.Model):
    
    def __str__(self):
        return self.text