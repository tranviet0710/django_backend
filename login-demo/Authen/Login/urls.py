from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('login/', views.LoginClass.as_view(), name='login'),
    path('user-view/', views.ViewUser.as_view(), name='user_view')
]
