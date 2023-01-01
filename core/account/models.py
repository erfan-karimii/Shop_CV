from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager ,PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
import re
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,phone_number,password,**extra_fields):
        """
        Creates and saves a User with the given phone_number , password and extra fields.
        """
        if not phone_number:
            raise ValueError(_("the phone_number must be set"))
        # user = self.model(phone_number=phone_number,**extra_fields)
        user = User(phone_number=phone_number,**extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,phone_number,password,**extra_fields):
        """
        Creates and saves a superuser with the given phone_number , password and extra fields.
        """
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_verified',True)


        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Superuser must have staff=True."))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Superuser must have superuser=True."))
    
        return self.create_user(phone_number,password,**extra_fields)



def validate_phone_number(value):
    if  not bool(re.compile("^(?:0|98|\+98|\+980|0098|098|00980)?(9\d{9})$").match(value)):
        raise ValidationError(
            _('number is not valid'),
        )

class User(AbstractBaseUser,PermissionsMixin):
    '''
    Custom User Model for our app
    '''
    phone_number = models.CharField(max_length=15,unique=True,validators=[validate_phone_number])
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    USERNAME_FIELD = 'phone_number'

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    objects = UserManager()
    def __str__(self):
        return self.phone_number


class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    full_name  = models.CharField(max_length=400)
    email = models.EmailField()
    address = models.TextField()

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.phone_number

@receiver(post_save,sender=User)
def save_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)