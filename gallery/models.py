from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class event(models.Model):
    Event = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to='pics/gallery', default='pics/gallery/default.jpg')

    def __str__(self):
        return self.Event


class gallery(models.Model):
    event = models.ForeignKey(
        event, default=1, verbose_name="Event", on_delete=models.CASCADE)
    img = models.ImageField(upload_to='pics/gallery', default='pics/gallery/default.jpg')
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Galleries"

    def __str__(self):
        return self.description
