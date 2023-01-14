from django.db import models
from product.models import Product
from colorfield.fields import ColorField
from django.contrib.auth import get_user_model

# Create your models here.
MyUser=get_user_model()


class Order(models.Model):
    owner = models.ForeignKey(MyUser,on_delete=models.CASCADE,null=True)
    is_paid = models.BooleanField(default=False)
    payment_date = models.DateTimeField(blank=True,null=True)
    full_name = models.CharField(max_length=250,null=True)
    address = models.TextField(null=True)



    def get_total_price(self):
        amount = 0 
        for detail in self.orderdetail_set.all():
            amount += detail.price * detail.count

        return amount

    def __str__(self):
        return str(self.owner)

class OrderDetail(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.IntegerField()
    color = ColorField(null=True)
    size = models.CharField(max_length=20,null=True)
    count = models.IntegerField()

    def get_detail_sum(self):
        return self.count * self.price

    def __str__(self):
        return str(self.order) + " "+ str(self.product)
