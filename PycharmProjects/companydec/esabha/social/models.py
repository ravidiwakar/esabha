from django.contrib.auth.models import User
from django.core.validators import RegexValidator, MinValueValidator
from django.db import models
# from django.utils.encoding import python_2_unicode_compatible


# Create your models here.
from django.db.models import CASCADE


class MyProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    phone_no = models.CharField(validators=[RegexValidator("^0?[5-9]{1}\d{9}$")], max_length=15, null=True, blank=True)
    address = models.TextField()
    pic = models.ImageField(upload_to= "images\\" ,null=True)
    status = models.CharField(max_length=20, default='single', choices=(("single","single"),('married','married'),('widow','widow'),('seprate','seprate'),('commited','commited')))
    gender = models.CharField(max_length=20,default='male', choices=(('male','male'),('female', 'female')))
    age = models.IntegerField(default=18, validators=[MinValueValidator(18)])
    description = models.TextField(null=True,blank=True)
    user = models.OneToOneField(to=User, on_delete=CASCADE)
    def __str__(self):
        return "%s" % self.user

class MyPost(models.Model):
    pic = models.ImageField(upload_to="images\\", null=True)
    subject = models.CharField(max_length=100)
    msg = models.TextField(null=True,blank=True)
    cr_date = models.DateField(auto_now_add=True)
    uploaded_by = models.ForeignKey(to=MyProfile, on_delete=CASCADE, null=True, blank=True)
    def __str__(self):
        return "%s" % self.subject


class FollowUser(models.Model):
    profile = models.ForeignKey(to=MyProfile, on_delete=CASCADE, related_name="profile")
    followed_by = models.ForeignKey(to=MyProfile, on_delete=CASCADE,related_name="followed_by")

    def __str__(self):
        return "%s" % self.followed_by




