from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
# Create your models here.


class event(models.Model):
    Event = models.CharField( max_length=50)

    def __str__(self):
        return self.Event

class services(models.Model):
    img = models.ImageField(upload_to='pics/services', blank=True, default='pics/about/default.jpg')
    day = models.CharField(max_length=50)
    event = models.ForeignKey(
        event, default=1, verbose_name="Event", on_delete=models.CASCADE)
    date = models.DateTimeField("date", default=datetime.now())
    description = RichTextField(max_length=100)
    state = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = "Services"

    def __str__(self):
        return self.day

class about(models.Model):
    img = models.ImageField(upload_to='pics/about', blank=True, default='pics/about/default.jpg')
    timeLine = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = RichTextField()

    def __str__(self):
        return self.title


class team(models.Model):
    img = models.ImageField(upload_to='pics/team', blank=True, default='pics/team/default.png')
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    twiter = models.URLField(max_length=256, blank=True)
    facebook = models.URLField(max_length=256, blank=True)

    def __str__(self):
        return self.name
