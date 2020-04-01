from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import quotes, event, book
import json
# Create your views here.


def quotes_page(request):
    data = {
        'quotes': quotes.objects.all(),
        'event': event.objects.all(),
        'book': book.objects.all()
    }
    return render(request, 'quotes.temp.html', data)


def quotes_filter(request):
    service = request.GET.get('selected')
    book = request.GET.get('book')

    if service != 'all' and book != 'all':
        quotes1 = quotes.objects.filter(event_id=service, book_id=book)
        event1 = event.objects.all()

    elif service == 'all' and book != 'all':
        quotes1 = quotes.objects.filter(book_id=book)
        event1 = event.objects.all()

    elif service != 'all' and book == 'all':
        quotes1 = quotes.objects.filter(event_id=service)
        event1 = event.objects.all()

    else:
        quotes1 = quotes.objects.all()
        event1 = event.objects.all()

    data = {'quotes': quotes1, 'events': event1}
    return render(request, 'quotes.filter.temp.html', data)
