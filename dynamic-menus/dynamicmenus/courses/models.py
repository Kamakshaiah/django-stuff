from django.db import models

# Create your models here.

class course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    features = models.TextField()

    def __str__(self):
        return self.name