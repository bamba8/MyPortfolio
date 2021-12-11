from django.shortcuts import render
from django.http import HttpResponseRedirect
import datetime


from .formulaire import PortfolioForm

from .models import Home, About, Profile, Category, Skills, Portfolio
from django.contrib import messages


def index(request):
    # HOME

    home = Home.objects.latest('updated')

    # About
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter()
    
    # Skills
    categories = Category.objects.all()

    # Portfolio
    portfolios = Portfolio.objects.all()

    context = {
        "home": home,
        "about": about,
        "profiles": profiles,
        "categories": categories,
        "portfolios": portfolios,

    }
    
    return render(request, "index.html", context)


def send_message(request):

    if request.method == "POST":
        form = PortfolioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, " Votre message a été envoyé avec succès !")
            return HttpResponseRedirect(request.path)

    else:
        form = PortfolioForm
    return render(request, "contact/contact.html", {"form": form})























    
