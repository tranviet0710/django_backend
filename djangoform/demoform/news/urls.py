from django.urls import path, include
from . import views

app_name = "news"
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_post, name='add'),
    path('save/', views.save_news, name='save'),
    path('email/', views.send_email, name='send'),
    path('emailInFo',  views.show_email, name='showEmail')
]
