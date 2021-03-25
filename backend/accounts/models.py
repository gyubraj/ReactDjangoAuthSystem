from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

class UserAccountManager(BaseUserManager):
    def create_user(self,email,password=None,**extra_fields):
        if not email:
            return
            raise ValueError("User must provide Email")
        email=self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self,email,password=None,**extra_fields):
        if not email:
            return
            raise ValueError("Enter Valid Email")

        email=self.normalize_email(email)
        user=self.model(email=email,is_superuser=True,is_staff=True,**extra_fields)
        user.set_password(password)
        user.save()
        return user



class UserAccount(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(max_length=255,unique=True)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser =models.BooleanField(default=False)
    deactivate=models.BooleanField(default=False,null=True,blank=True)

    objects=UserAccountManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['first_name','last_name']

    def get_full_name(self):
        return self.first_name

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email

    # @property
    # def address(self):
    #     return self.address_set.all()

    # @property
    # def profile(self):
    #     return self

class Address(models.Model):
    user=models.OneToOneField(UserAccount,on_delete=models.CASCADE)
    country=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    street=models.CharField(max_length=20)

    def __str__(self):
        return self.user.email

class Profile(models.Model):
    class PublicProfiles(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(public=True)
    user=models.OneToOneField(UserAccount,on_delete=models.CASCADE)
    public=models.BooleanField(default=True)
    bio=models.TextField(max_length=255,null=True,blank=True)
    objects=models.Manager()  #Default
    publicprofiles=PublicProfiles()  #Custom


    def __str__(self):
        return self.user.email


@receiver(post_save,sender=UserAccount)
def user_is_created(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
        Address.objects.create(user=instance)
    else:
        instance.profile.save()
        instance.address.save()



# # I will delete this
# class Messages(models.Model):
#     user=models.ForeignKey(UserAccount,on_delete=models.CASCADE)
#     message=models.CharField(max_length=100,null=True,blank=True)
#
#     def __str__(self):
#         return self.message