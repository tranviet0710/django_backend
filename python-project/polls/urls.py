from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    # path('', views.index1, name='index1'),
    # path('child', views.index2, name='index2'),
    # path('childTemplate', views.index3, name='index3'),
    # path('questionList', views.questionList_view, name='questionList'),
    # path('questionDetail/<int:question_id>', views.detailView, name='questionDetail'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    # path('<int:question_id>/result/', views.result, name='result'),


    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
