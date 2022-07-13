from distutils.command.upload import upload
from pyexpat import model
from typing import Set
from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    def __str__(self):
        return f'{self.name} ({self.address})'
class Participant(models.Model):
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.email
#one to one and one to many or many to many right now we are dealing with one to many.....as a location can have many meetups
#but a meetup can have only one location
class Meetup(models.Model):
    title = models.CharField(max_length=200)
    #organizer_email = models.EmailField()
    #date = models.DateField()
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)    
    participants = models.ManyToManyField(Participant, blank=True )
    def __str__(self):
        return f'{self.title}-{self.slug}'