from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('login/', views.LoginClass.as_view(), name='login')
]
