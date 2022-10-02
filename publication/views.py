from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurant
from .models import Grade
from .forms import ReviewForm

def pub(request):
    items = Restaurant.objects.all()
    context = {
        'items':items
    }
    return render(request, "restaurant/pub.html", context)

def review(request, id):
    