from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('polls/', include("polls.urls")),
    path('polls2/', include("polls2.urls")),
    path('admin/', admin.site.urls),
    path('', admin.site.urls),
]
