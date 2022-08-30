from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='company/%y/%m/%d')
    subtitle = models.CharField(max_length=500)
    fb_link = models.URLField(null=True,blank=True)
    insta_link = models.URLField(null=True,blank=True)
    tw_link = models.URLField(null=True,blank=True)
    address = models.TextField(max_length=500)
    phone_numper = models.TextField(max_length=500)
    email = models.TextField(max_length=500)
    call_us = models.CharField(max_length=500)
    email_us = models.EmailField()
    
    def __str__(self) -> str:
        return self.name
    