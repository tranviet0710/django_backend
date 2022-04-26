from django.shortcuts import render
from django.http import HttpResponse, request
from .forms import PostForm, SendEmail
from django.views import View

# Create your views here.

class Index(View):
    def get(self, request):
        return HttpResponse("Hello World")

def add_post(request):
    a = PostForm()
    return render(request, 'news/add_news.html', {'f': a})

class AddPost(View):
    def get(self, request):
        a = PostForm()
        return render(request, 'news/add_news.html', {'f':a})

def save_news(request):
    if request.method == "POST":
        g = PostForm(request.POST)
        if g.is_valid():
            g.save()
            return HttpResponse("Saved!")
        else:
            return HttpResponse("Not validated")
    else:
        return HttpResponse("Not post request!")

class SaveNews(View):
    def post(self, request):
        g = PostForm(request.POST)
        if g.is_valid():
            g.save()
            return HttpResponse("Saved!")
        else:
            return HttpResponse("Not validated")

def send_email(request):
    g = SendEmail()
    return render(request, "news/send_email.html", {"f": g})

class Send_Email(View):
    def get(self, request):
        g = SendEmail()
        return render(request, 'news/send_email.html', {'f':g})

def show_email(request):
    if request.method == "POST":
        g = SendEmail(request.POST)
        if g.is_valid():
            # title = g.cleaned_data['title']
            # email = g.cleaned_data['email']
            # content = g.cleaned_data['content']
            # cc = g.cleaned_data['cc']
            # info = {"title": title, "email": email, "content": content, "cc": cc}
            return render(request, 'news/email_info.html', {"info" : g})
        else:
            return HttpResponse("Not validated")
    else:
        return HttpResponse("Not post request!")

class ShowEmail(View):
    def post(self, request):
        g = SendEmail(request.POST)
        if g.is_valid():
            return render(request, 'news/email_info.html', {"info": g})
        else:
            return HttpResponse("Not validated!")