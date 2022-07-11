from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    date_of_birth=models.DateField(null=True)
    is_authenticated = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)