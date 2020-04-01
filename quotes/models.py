from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from django.utils import timezone
# Create your models here.


class event(models.Model):
    Event = models.CharField(max_length=50)

    def __str__(self):
        return self.Event

class book(models.Model):
    Book = models.CharField(max_length=50)

    def __str__(self):
        return self.Book


class quotes(models.Model):
    date = models.DateField(("Date"), default=timezone.now)
    event = models.ForeignKey(
        event, default=1, verbose_name="Event", on_delete=models.CASCADE)
    quote = RichTextField()
    book = models.ForeignKey(book, default=1, verbose_name="Book", on_delete=models.CASCADE)
    verse = models.IntegerField()
    frm = models.IntegerField()
    to = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Quotes"

    def __str__(self):
        return self.book.Book
