from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class AboutUsGeneral(models.Model):
    title1 = models.CharField(max_length=155)
    title2 = models.CharField(max_length=155) 
    title3 = models.CharField(max_length=155) 
    text1 = models.TextField()
    text2 = models.TextField()
    text3 = models.TextField()
    video = models.FileField(null=True)
    video_bg_image = models.ImageField(null=True)
    image1 = models.ImageField()
    alt1 = models.CharField(max_length=50) 
    image2 = models.ImageField()
    alt2 = models.CharField(max_length=50)
    active = models.BooleanField(default=True) 

class AboutUsProperty(models.Model):
    title = models.CharField(max_length=155)
    text = models.TextField()
    
    def __str__(self):
        return self.title

class AboutUsProgressBar(models.Model):
    title = models.CharField(max_length=155)
    percentage = models.IntegerField(validators=[MaxValueValidator(100),MinValueValidator(0)],default=0)
    
    def __str__(self):
        return self.title

