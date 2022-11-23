from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band, Listing

# Create your views here.
def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})

def band_detail(request, band_id):
    band = Band.objects.get(id=band_id)
    listings = Listing.objects.all()
    return render(request, 'listings/band_detail.html', {'band': band, 'listings': listings})


def about(request):
    return HttpResponse('<h1>Sobre nós</h1><p>Somos uma loja online ...</p>')
