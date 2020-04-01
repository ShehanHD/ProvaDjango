from django.shortcuts import render
from .models import gallery, event

# Create your views here.
def album(request):
    data = {
        'gallery':gallery.objects.all(),    
        'event':event.objects.all(), 
    }

    return render(request, 'galleryBody.temp.html', data)

def photos(request):
    if request.method == 'GET':
        req = request.GET.get('selected')

        if req == 'null':
            filterGal = gallery.objects.all()
        else:
            filterGal = gallery.objects.filter(event_id=req)

    data = {
        'gallery':filterGal,
    }

    return render(request, 'galleryAlbum.temp.html',data)

def allPhotos(request):
    data = {
        'gallery':gallery.objects.all(),  
        'event':event.objects.all(),   
    }

    return render(request, 'galleryAlbum.temp.html',data)