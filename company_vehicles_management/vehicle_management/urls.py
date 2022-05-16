from django.urls import path

from .views import *

urlpatterns = [
    path('', get_list_vehicle, name='vehicles'),
    path('create/', create_new_vehicle, name='create'),
    path('create_category/', create_new_category, name='create_category'),
    path('detail/<int:id>', vehicle_detail, name='detail'),
    path('delete/<int:id>', vehicle_delete, name='delete'),
    path('update/<int:id>', vehicle_update, name='update'),
    path('search', search_vehicle, name='search'),
]
