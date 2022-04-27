from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate
# Create your views here.
class Index(View):
    def get(self, request):
        return HttpResponse("<h1>Xin Chao</h1>")

class LoginClass(View):
    def get(self, request):
        return render(request, 'Login/login.html')
    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        account = authenticate(username=username, password=password)
        if account is None:
            return HttpResponse("Account is not existed")
        return HttpResponse("Login with %s %s" %(username,password))
