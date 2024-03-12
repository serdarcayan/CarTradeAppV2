from django.shortcuts import render
from django.http import HttpResponse
from home.models import Settings
from ilanlar.models import Ilanlar

# Create your views here.


def detail(request, id):
    return HttpResponse(id)


def index(request):
    sett = Settings.objects.get(pk=1)
    deals = Ilanlar.objects.all().order_by('create_time').reverse()
    slider = Ilanlar.objects.order_by('?')[:3]
    for deal in deals:
        deal.price = '{:,}'.format(deal.price).replace(',', '.')
        deal.km = '{:,}'.format(deal.km).replace(',', '.')
    context = {
        "sett": sett,
        "Page": "home",
        "deals": deals,
        }
    return render(request, "index.html", context)
  