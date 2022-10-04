from django.urls import path
from . import views

urlpatterns = [
    path('', views.pub, name='pub.index'),
    path('success',views.success, name="success"),
    path('rate/<int:id>',views.rate,name="rate"),
]