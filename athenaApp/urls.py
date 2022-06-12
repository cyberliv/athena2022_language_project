from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webApp.urls')),
    path('messages/', include('postman.urls')),
]