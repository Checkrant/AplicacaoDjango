
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('', include('main.urls')),
    path('users/', include('users.urls')),
    path('publication/', include('publication.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls'))
]
