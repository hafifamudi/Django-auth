from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='userprofileinfo')

    first_name = models.CharField(max_length=10, default='')
    last_name = models.CharField(max_length=10, default='')
    email = models.CharField(max_length=20, default='')
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to="profile_pics",blank=True, null=True)

    def __str__(self):
        return self.first_name
    
    class Meta:
        db_table = 'userprofileinfo'