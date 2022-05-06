from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.views import generic
# Create your view here.

# def index1(request):
#     return HttpResponse("Response to request 1 in polls1")
#
# def index2(request):
#     return HttpResponse("Response to request 2 in polls1")
#
# def index3(request):
#     myname = "Viet Dev"
#     taisan ={"sach", "vo", "but", "cap"}
#     dic = {"name": myname, "taisan":taisan}
#     return render(request, "polls/index.html", dic)
#
# def questionList_view(request):
#     #listQuestions = get_list_or_404(Question, pk=1)
#     question_list = Question.objects.all()
#     context = {"questionList": question_list}
#     return render(request, "polls/question_list.html", context)
#
# def detailView(request, question_id):
#     question = get_object_or_404(Question, pk = question_id)
#     return render(request, "polls/detail_question.html", {"question": question})
#
def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        # get id of choice in choice set
        selected_choice_id = request.POST["choice"]
        selected_choice = question.choice_set.get(pk = selected_choice_id)
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail_question.html', {
            'question': question,
            'error_message': 'You didnt select a choice.'
        })
    selected_choice.vote += 1
    selected_choice.save()
    #return render(request, 'polls/result.html', {"question": question})
    return HttpResponseRedirect(reverse('polls:result', args=(question_id, )))

def result(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/result.html', {"question": question})

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'