from django.db import models

# Create your models here.

class ContactUsKeeper(models.Model):
    full_name = models.CharField(max_length=155)
    email = models.EmailField(max_length=155)
    subject = models.CharField(max_length=155)
    message = models.TextField()

    def __str__(self):
        return self.subject
    
class Newsletter(models.Model):
    email = models.EmailField(max_length=155,unique=True)

    def __str__(self):
        return self.email
