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
        "rasgele_ilanlar":rasgele_ilanlar,
        }
    return render(request, "index.html", context)

def hakkimizda(request):
    sett = Settings.objects.get(pk=1)
    context = {
        "Page": "hakkimizda",
        "title": "CarVilla | Hakkimizda",
        "sett": sett,
        }

    return render(request, "hakkimizda.html", context)

def format_phone_number(phone):
    formatted_phone = "{}({}) {} {} {}".format(
        phone[0], phone[1:4], phone[4:7], phone[7:9], phone[9:]
    )
    return formatted_phone

def iletişim(request):
    sett = Settings.objects.get(pk=1)
    sett_phone = format_phone_number(sett.phone)
    context = {
        "Page": "iletişim",
        "title": "CarVilla | iletişim",
        "sett": sett,
        "sett_phone": sett_phone,
    }

    return render(request, "iletisim.html", context)