from django.http import HttpResponse
from django.shortcuts import redirect, render
from home.models import Settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.


def profile(request):
    return HttpResponse("Profile")


def user_login(request):
    sett = Settings.objects.get(pk=1)
    if request.user.is_authenticated:
        return redirect("index")
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(request, username=username, email=email, password=password)

        if user is not None:
            login(request, user)

        else:
            return render(
                request,
                "login.html",
                {
                    "error": "Girilen değerlere ait hesap bulunamadı!",
                    "title": "CarVilla | Giriş yap",
                    "sett": sett,
                },
            )

    context = {
        "title": "CarVilla | Giriş yap",
        "sett": sett,
    }

    return render(request, "login.html", context)


def user_register(request):
    sett = Settings.objects.get(pk=1)
    if request.user.is_authenticated:
        return redirect("index")
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        passwordagain = request.POST["passwordagain"]
        sozlesmeonay = request.POST.get("sozlesmeonay")

        if not sozlesmeonay:
            return render(
                request,
                "register.html",
                {
                    "error": "Sözleşmeyi onaylamadan kayıt olamazsınız.",
                    "username": username,
                    "email": email,
                },
            )
        else:
            if password == passwordagain:
                if User.objects.filter(username=username).exists():
                    return render(
                        request,
                        "register.html",
                        {
                            "error": "Kullanıcı adı kulanılıyor. Lütfen başka bir kullanıcı adı ile deneyiniz:",
                            "username": username,
                            "email": email,
                        },
                    )
                else:
                    if User.objects.filter(email=email).exists():
                        return render(
                            request,
                            "register.html",
                            {
                                "error": "E-mail adresine ait hesap bulunmakta",
                                "username": username,
                                "email": email,
                            },
                        )
                    else:
                        user = User.objects.create_user(
                            username=username, email=email, password=password
                        )
                        user.save()
                        return render(
                            request,
                            "login.html",
                            {
                                "success": "Kullanıcı hesabı başarıyla oluşturuldu!",
                                "username": username,
                                "email": email,
                            },
                        )
            else:
                return render(
                    request, "register.html", {"error": "Parolalar eşleşmiyor!"}
                )

    context = {
        "title": "CarVilla | Kayıt ol",
        "sett": sett,
    }

    return render(request, "register.html", context)


def user_logout(request):
    logout(request)
    return redirect("index")


def favilanlar(request):
    return HttpResponse("favilanlar")


def ilanolustur(request):
    return HttpResponse("ilanolustur")
