from django.shortcuts import render, redirect

# Create your views here.

from basic.models import Url
from .forms import Urlform
from .shortner import Urlx
import random


def Make(request):
    form = Urlform(request.POST)
    a = ''
    if request.method == 'POST':
        if form.is_valid():
            Newurl = form.save(commit=False)
            a = Urlx().short(random.choice('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))
            Newurl.short_url = a
            Newurl.save()
        else:
            form = Urlform()
            a = "Invalid URL"
    return render(request, 'urlshort.html', {'form': form, 'a':a})


def Home(request, token):
    try:
        original_url = Url.objects.filter(short_url=token)[0]
        return redirect(original_url.original_url)
    except IndexError as error:
        return render(request, 'urlshort.html')
    
    
        
    