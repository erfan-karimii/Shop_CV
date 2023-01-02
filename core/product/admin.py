from django.contrib import admin
from .models import Product , Category , TagProduct , Color , Size , GalleryImage
# Register your models here.

class Color2(admin.TabularInline):
    model = Color
    extra = 0

class Size2(admin.TabularInline):
    model = Size
    extra = 0

class GalleryImage2(admin.TabularInline):
    model = GalleryImage
    extra = 0

class CustomProduct(admin.ModelAdmin):
    inlines = [Color2,Size2,GalleryImage2]


admin.site.register(Product,CustomProduct)
admin.site.register(Category)
admin.site.register(TagProduct)


