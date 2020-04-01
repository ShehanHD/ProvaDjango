from django.shortcuts import render
from django.core.mail import EmailMessage, send_mass_mail
from django.http import JsonResponse

from .models import event, services, about, team

# Create your views here.


def home(request):
    data = {
        'services':services.objects.all(),
        'event':event.objects.all(),
        'about':about.objects.all(),
        'team':team.objects.all(),
    }

    return render(request, 'index.temp.html',  data)

def feedback(request):
    if request.method == 'GET':
        name = request.GET.get('name')
        email = request.GET.get('email')
        phone = request.GET.get('phone')
        msg = request.GET.get('msg')

    reply = 'Thank you '+name+' for contacting us'

    message1 = (name, msg, 'wecode.server@gmail.com', ['shehanhd2018@gmail.com'])
    message2 = ('Greetigns!', reply, 'wecode.server@gmail.com', [email])

    send_mass_mail((message1, message2), fail_silently=False) 

    data={'name':name}
        
    return JsonResponse(data)
