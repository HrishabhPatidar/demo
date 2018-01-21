# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Discription(models.Model):
    discription = models.CharField(max_length = 150)


class Gallery(models.Model):
    discription = models.CharField(max_length = 150)
    gallery_images = models.ImageField(upload_to = 'images/gallery')
    def __set__(self):
        return self.gallery_images


class Registrationdetails(models.Model):
    pdf = models.FileField(upload_to='reg_detail')
# this is only for only for backup purpose
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_no = models.IntegerField()
    message = models.CharField( max_length=20000)
