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
    MEDIA_ROOT = os.path.join(BASE_DIR,'thumnail')
    if platform.system() == 'Windows':
        return f'{MEDIA_ROOT}\{basefilename}{file_extension}'
    else:
        return f'{MEDIA_ROOT}/{basefilename}{file_extension}'

class Category(models.Model):
    name = models.CharField(max_length=200,verbose_name='نام دسته بندی')
    image = models.ImageField(blank=True,null=True)

    def __str__(self):
        return self.name
# test


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
    # descriptions = models.CharField(max_length=300)
    image = models.ImageField()
    alt = models.CharField(max_length=100)
    image_2 = models.ImageField(blank=True,null=True)
    alt_2 = models.CharField(max_length=100,null=True,blank=True)
    price = models.IntegerField(verbose_name='قیمت اصلی')
    product_count = models.PositiveBigIntegerField(verbose_name='تعداد محصول',validators=[MinValueValidator(0)])
    category = models.ForeignKey(Category,on_delete=models.PROTECT)
    info = RichTextField()
    # more_info = RichTextField(null=True)
    tag = models.ManyToManyField(TagProduct)
    takhfif = models.IntegerField(validators=[MaxValueValidator(100),MinValueValidator(0)],verbose_name='درصد تخفیف',default=0)
    orgin_color = ColorField(samples=COLOR_PALETTE)
    orgin_size = models.CharField(max_length=20)
    created  =models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True,null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def main_discount_cal(self):
        # if inti:
        return int(self.price - (self.price * (self.takhfif/100)))
        # return self.price - (self.price * (self.takhfif/100))
    
    def save(self):
        super().save()  # saving image first
        img = Image.open(self.image.path)  # Open image using self 
        new_image = img.resize((1000, 1000))
        x = photo_path(str(self.image))   
        new_image.save(x)  # saving image at the same path

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
    
    # def color_price_cal(self):
    #     return self.Ekhtelaf + self.product.price - (self.product.price * (self.product.takhfif/100))

class GalleryImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.PROTECT)
    image = models.ImageField(verbose_name='عکس محصول',unique=True)
    alt = models.CharField(max_length=150,verbose_name='توضیحات عکس')
    
    def __str__(self):
        return str(self.image)
    
    def save(self):
        # super().save()  
        img = Image.open(self.image.path)  # Open image using self 
        new_image = img.resize((1000, 1000))
        x = photo_path(str(self.image))   
        new_image.save(x)  # saving image at the same path

# class Comment(models.Model):
#     product = models.ForeignKey(Product,on_delete=models.CASCADE)
#     parent = models.ForeignKey('self',null=True,blank=True,default=None,on_delete=models.SET_NULL)
#     username = models.CharField(max_length=100,null=True)
#     title = models.CharField(max_length=100)
#     body = models.TextField()
#     like = models.PositiveIntegerField(validators=[MaxValueValidator(1000)],default=0,null=True)
#     created = models.DateTimeField(auto_now=True)
#     is_show = models.BooleanField(default=False)
    
#     def __str__(self):
#         return self.username
    
#     class Meta :
#         ordering = ['created']