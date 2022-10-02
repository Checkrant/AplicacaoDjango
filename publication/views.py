from django.shortcuts import render, redirect
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
    post = Restaurant.objects.get(id=id)
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        restaurant_name = request.POST.get('restaurant_name')
        stars = request.POST.get('stars')
        detail = request.POST.get('detail')
        grade = Grade(restaurant_name=restaurant_name, stars=stars,  detail=detail , restaurant=post)
        grade.save()
        return redirect('success')
    
    form = ReviewForm()
    context = {
        "form":form
    }
    return render(request, 'restaurant/review.html',context)

def success(request):
    return render(request, "restaurant/success.html")