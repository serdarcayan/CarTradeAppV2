from django.shortcuts import render
from django.http import HttpResponse
from home.models import Settings
from ilanlar.models import Ilanlar

# Create your views here.

def index(request):
    sett = Settings.objects.get(pk=1)
    deals = Ilanlar.objects.all().order_by('create_time').reverse()[:8]
    rasgele_ilanlar = Ilanlar.objects.order_by('?')[:8]
    for deal in deals:
        deal.price = '{:,}'.format(deal.price).replace(',', '.')
        deal.km = '{:,}'.format(deal.km).replace(',', '.')

    for deal in rasgele_ilanlar:
        deal.price = '{:,}'.format(deal.price).replace(',', '.')
        deal.km = '{:,}'.format(deal.km).replace(',', '.')

    context = {
        "sett": sett,
        "Page": "home",
        "deals": deals,
        'rasgele_ilanlar':rasgele_ilanlar,
        }
    return render(request, "index.html", context)

def hakkimizda(request):
    
    context = {
        "Page": "hakkimizda",
        "title": "Hakkimizda",
        }

    return render(request, "hakkimizda.html", context)
  
def iletişim(request):
    sett = Settings.objects.get(pk=1)
    context = {
        "Page": "iletişim",
        "title": "iletişim",
        "sett":sett,
        }

    return render(request, "iletisim.html", context)