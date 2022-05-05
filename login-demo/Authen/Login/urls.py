from django.urls import path

from . import views

#namespacing url names for each app
#used to differentiate which app to call url in templates
app_name = 'Login'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('login/', views.LoginClass.as_view(), name='login'),
    path('user-view/', views.ViewUser.as_view(), name='user_view'),
    path('add-post/', views.AddPost.as_view(), name='add_post'),
]
