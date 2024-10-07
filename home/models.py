from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    phone=models.IntegerField()
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return f"{self.name}"
