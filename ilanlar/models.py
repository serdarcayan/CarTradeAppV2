from django.db import models

import uuid

# Create your models here.


class Brands(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to="images/")
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title


class Ilanlar(models.Model):
    def generate_slug():
        return str(uuid.uuid4()).replace("-", "")
    STATUS = (("True", "Aktif"), ("False", "Deaktif"))
    GEARBOX_TYPE = (
        ("manual", "Manual"),
        ("automatic", "Automatic"),
    )
    title = models.CharField(max_length=255, blank=False)
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE, blank=False)
    banner = models.ImageField(upload_to="images/", blank=False)
    images = models.ImageField(upload_to="images/", blank=False, default=None)
    model = models.PositiveSmallIntegerField(default=1900, blank=False)
    km = models.IntegerField(default=0, blank=False)
    horsepower = models.IntegerField(default=10, blank=False)
    Gearbox = models.CharField(max_length=20, choices=GEARBOX_TYPE, default="manual", blank=False)
    description = models.TextField(blank=False)
    price = models.IntegerField(default=0, blank=False)
    create_time = models.DateTimeField(auto_now_add=True,editable=False)
    slug = models.SlugField(null=False, unique=True, default=generate_slug, blank=False)
    status = models.CharField(max_length=10, choices=STATUS, default="True", blank=False)
    goruntulenme_sayisi = models.IntegerField(default=0,editable=False)

    def __str__(self):
        return self.title