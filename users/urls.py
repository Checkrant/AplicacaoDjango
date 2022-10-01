from django.urls import path
from .views import UserCreateView, UserRantCreateView

urlpatterns = [


    path('userForm/', UserCreateView.as_view(), name='user.index'),
    path('rantForm/', UserRantCreateView.as_view(), name='rant.index'),
    
  
]