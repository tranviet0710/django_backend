from django.urls import path

from . import views

app_name = "news"
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('add/', views.AddPost.as_view(), name='add'),
    path('email/', views.Send_Email.as_view(), name='send'),
    path('emailInFo', views.ShowEmail.as_view(), name='showEmail')
]
