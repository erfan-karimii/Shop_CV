from django.db import models
from ckeditor.fields import RichTextField
from colorfield.fields import ColorField
from django.core.validators import MaxValueValidator, MinValueValidator
from PIL import Image
import os
from core.settings import BASE_DIR
import platform
from django.http import HttpResponse

def photo_path(filename):
    basefilename, file_extension = os.path.splitext(filename)
    # random_text = ''.join([choice(string.ascii_letters) for _ in range(5)])
    MEDIA_ROOT = os.path.join(BASE_DIR,'thumbnail')
    if platform.system() == 'Windows':
        return f'{MEDIA_ROOT}\{basefilename}{file_extension}'
    else:
        return f'{MEDIA_ROOT}/{basefilename}{file_extension}'

class Category(models.Model):
    name = models.CharField(max_length=200,verbose_name='نام دسته بندی')
    image = models.ImageField(blank=True,null=True)

    def __str__(self):
        return self.name

class TagProduct(models.Model):
    name =models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    COLOR_PALETTE = [
        ("#FFFFFF", "white", ),
        ("#000000", "black", ),
    ]
    name = models.CharField(max_length=250)
    image = models.ImageField()
    alt = models.CharField(max_length=100)
    image_2 = models.ImageField(blank=True,null=True)
    alt_2 = models.CharField(max_length=100,null=True,blank=True)
    price = models.IntegerField(verbose_name='قیمت اصلی')
    product_count = models.PositiveBigIntegerField(verbose_name='تعداد محصول',validators=[MinValueValidator(0)])
    category = models.ForeignKey(Category,on_delete=models.PROTECT)
    info = RichTextField()
    tag = models.ManyToManyField(TagProduct)
    discount = models.IntegerField(validators=[MaxValueValidator(100),MinValueValidator(0)],verbose_name='درصد تخفیف',default=0)
    orgin_color = ColorField(samples=COLOR_PALETTE)
    orgin_size = models.CharField(max_length=20)
    created  =models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True,null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def main_discount_call(self):
        return int(self.price - (self.price * (self.discount/100)))
    
    def save(self):
        super().save()  # saving image first
        img = Image.open(self.image.path)  # Open image using self 
        new_image = img.resize((350, 280))
        x = photo_path(str(self.image))   
        new_image.save(x)  # saving image at the thumnail path

class Size(models.Model):
    product = models.ForeignKey(Product,on_delete=models.PROTECT)
    size = models.CharField(max_length=20,verbose_name='سایز')
    Ekhtelaf = models.IntegerField(verbose_name='اختلاف قیمت',default=0)

    class Meta:
        verbose_name='سایز های بیشتر کیف'
        verbose_name_plural='سایز های بیشتر کیف'

    def __str__(self):
        return self.size

class Color(models.Model):
    COLOR_PALETTE = [
        ("#FFFFFF", "white", ),
        ("#000000", "black", ),
    ]
    product = models.ForeignKey(Product,on_delete=models.PROTECT)
    color = ColorField(samples=COLOR_PALETTE)
    Ekhtelaf = models.IntegerField(verbose_name='اختلاف قیمت',default=0) 

    class Meta:
        verbose_name='رنگ های بیشتر'
        verbose_name_plural='رنگ های بیشتر'
    

    def __str__(self):
        return self.product.name + " " + self.color

class GalleryImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.PROTECT)
    image = models.ImageField(verbose_name='عکس محصول',unique=True)
    alt = models.CharField(max_length=150,verbose_name='توضیحات عکس')
    
    def __str__(self):
        return str(self.image)
    
    def save(self):
        super().save()  
        img = Image.open(self.image.path)  # Open image using self 
        new_image = img.resize((1000, 1000))
        x = photo_path(str(self.image))   
        new_image.save(x)  # saving image at the calculated path

class Comment(models.Model):
    star_choice = (
        (1,1),(2,2),(3,3),(4,4),(5,5)
    )
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    username = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=254,null=True)
    body = models.TextField()
    point = models.IntegerField(default=1,choices=star_choice)
    created = models.DateTimeField(auto_now=True)
    is_show = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username
    
    class Meta :
        ordering = ['created']
