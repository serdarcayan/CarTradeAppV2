from django.shortcuts import render, get_object_or_404
from home.models import Settings
from ilanlar.models import Brands, Ilanlar

# Create your views here.


def ilan(request):
    sett = Settings.objects.get(pk=1)
    brands = Brands.objects.all().order_by("title")
    deals = Ilanlar.objects.all()

    for deal in deals:
        deal.price = "{:,}".format(deal.price).replace(",", ".")
        deal.km = "{:,}".format(deal.km).replace(",", ".")

    context = {
        "Page": "ilan",
        "title": "CarVilla | ilanlar",
        "brands": brands,
        "deals": deals,
        "sett":sett,
    }

    return render(request, "ilanlar.html", context)


def ilan_detayi(request, slug):
    sett = Settings.objects.get(pk=1)
    deals = Ilanlar.objects.filter(slug=slug)
    context = {
        "Page": "ilan_detayi",
        "title": "CarVilla | İlan detayı",
        "deals": deals,
        "sett":sett,
    }

    return render(request, "ilan_detay.html", context)
