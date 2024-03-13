from django.db import models

# Create your models here.


class Settings(models.Model):

    title = models.CharField(max_length=90)
    icon = models.ImageField(blank=True, upload_to='images/')
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    fax = models.CharField(max_length=13)
    email = models.CharField(max_length=150)
    smtpserver = models.CharField(max_length=25)
    smtpemail = models.CharField(max_length=255)
    smtppassword = models.CharField(max_length=255)
    smtpport = models.CharField(max_length=10)
    facebook = models.CharField(max_length=150,default="facebook")
    instagram = models.URLField(max_length=150,default="instagram")
    twitter = models.CharField(max_length=150,default="twitter")
    linkedin = models.CharField(max_length=150,default="linkedin")
    aboutus = models.TextField(max_length=255)
    aboutus = models.TextField(max_length=255)
    referances = models.TextField(max_length=255)
    


    def __str__(self):
        return self.title