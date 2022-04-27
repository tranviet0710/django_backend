from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    path('', views.index1, name='index1'),
    path('child', views.index2, name='index2'),
    path('childTemplate', views.index3, name='index3'),
    path('questionList', views.questionList_view, name='questionList'),
    path('questionDetail/<int:questionID>', views.detailView, name='questionDetail'),
    path('<int:questionID>', views.vote, name='vote')
]
