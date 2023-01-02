from django.db import models



class SiteSetting(models.Model):
    logo = models.FileField(null=True,verbose_name='لوگو')
    alt = models.CharField(max_length=100,null=True,verbose_name='توضیحات لوگو')
    favicon = models.FileField(null=True,verbose_name='آیکون')
    alt2 = models.CharField(max_length=100,null=True,verbose_name='توضیحات icon')
    telephon = models.CharField(max_length=30,null=True,verbose_name='تلفن')
    footer_text = models.CharField(max_length=300,null=True,verbose_name='متن فوتر')
    email = models.EmailField(max_length=100,null=True,verbose_name='ایمیل')
    address = models.CharField(max_length=200,null=True,verbose_name='ادرس')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False,verbose_name='تنظیمات فعال؟')

    # def __str__(self):
    #     return self.email

class NavOne(models.Model):
    name = models.CharField(max_length=100,verbose_name='نام نوبار')
    link = models.CharField(max_length=100,verbose_name='لینک نوبار')    
    def __str__(self):
        return self.name

class NavTwo(models.Model):
    parent = models.ForeignKey(NavOne,on_delete=models.PROTECT)
    name = models.CharField(max_length=100,verbose_name='نام نوبار')
    link = models.CharField(max_length=100,verbose_name='لینک نوبار')    
    def __str__(self):
        return self.name

class Slider(models.Model):
    text1 = models.CharField(max_length=300,null=True,verbose_name='متن یک')
    text2= models.CharField(max_length=300,null=True,verbose_name='متن دو')
    text3= models.CharField(max_length=300,null=True,verbose_name='متن سه')
    image = models.ImageField(verbose_name='عکس سلایدر')
    alt = models.CharField(max_length=100,verbose_name='توضیح عکس')
    name_button = models.CharField(max_length=100,null=True,verbose_name='متن دکمه')
    link = models.CharField(max_length=100,null=True,verbose_name='ادرس دکمه')
    def __str__(self):
        return self.name_button + " | " + self.link

position = (
    ('right','راست'),
    ('left','چپ'),
    ('right2','راست (کنار محصولات)'),
)

class Tabligh(models.Model):
    image = models.ImageField()
    alt = models.CharField(max_length=50)
    text = models.CharField(max_length=100,null=True,verbose_name='متن')
    text2 = models.CharField(max_length=100,null=True,verbose_name='2متن')
    diraction = models.CharField(max_length=100,choices=position,verbose_name='مکان تبلیغ')
    link = models.CharField(max_length=400,null=True,verbose_name='لینک تبلیغ')
    def __str__(self):
        return self.text + " | " + self.link

class FooterOne(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class FooterTwo(models.Model):
    parent = models.ForeignKey(FooterOne,on_delete=models.PROTECT)
    name = models.CharField(max_length=50,verbose_name='نام')
    link = models.CharField(max_length=100,null=True,verbose_name='لینک صفحه')
    def __str__(self):
        return  str(self.parent.name) + " | " +  self.name 

class OnSale(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    image = models.ImageField()
    alt = models.CharField(max_length=50)
    date = models.DateField()
