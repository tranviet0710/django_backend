from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from .models import Question
# Create your view here.

def index1(request):
    return HttpResponse("Response to request 1 in polls1")

def index2(request):
    return HttpResponse("Response to request 2 in polls1")

def index3(request):
    myname = "Viet Dev"
    taisan ={"sach", "vo", "but", "cap"}
    dic = {"name": myname, "taisan":taisan}
    return render(request, "polls/index.html", dic)

def questionList_view(request):
    #listQuestions = get_list_or_404(Question, pk=1)
    listQuestions = Question.objects.all()
    context = {"questionList": listQuestions}
    return render(request, "polls/question_list.html", context)

def detailView(request, questionID):
    question = Question.objects.get(pk = questionID)
    return render(request, "polls/detail_question.html", {"question": question})

def vote(request, questionID):
    question = Question.objects.get(pk = questionID)
    try:
        choiceId = request.POST["choice"] #get id of choice in choice set
        choice = question.choice_set.get(pk = choiceId)
    except:
        HttpResponse("Loi khong co choice!")
    choice.vote = choice.vote + 1
    choice.save()
    return render(request, 'polls/result.html', {"question": question})
