from django.contrib.auth import authenticate, login, decorators
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


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
            return HttpResponse("Login Unsuccessfully! Account is not existed")

        login(request, account)

        return render(request, 'Login/successful.html')


class ViewUser(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        return HttpResponse("<h1>This is view user!</h1>")

    def post(self):
        pass


@decorators.login_required(login_url='/login/')
def view(request):
    return HttpResponse("View!!!")