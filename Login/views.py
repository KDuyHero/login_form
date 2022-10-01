from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, decorators
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm
# Create your views here.

class IndexClass(View):
    def get(self, request):
        return HttpResponse('<h1>Xin chào</h1>')

class LoginClass(View):
    def get(self, request):
        return render(request, 'Login/login_template.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is None: 
            return HttpResponse('user không tồn tại')
        
        login(request, user)
        return render(request,'Login/success.html')

class ViewUser(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        return HttpResponse('<h1>Đây là view user<h1>')


@decorators.login_required(login_url='login/')
def view_product(request):
    return HttpResponse('xem san pham')

class AddPost(LoginRequiredMixin,View):
    login_url ='/login/'
    def get(self, request):
        f =PostForm()
        context ={'fm':f}
        return render(request, 'login/add_post.html', context)

    def post(self, request):
        f = PostForm(request.POST)
        if not f.is_valid():
            return HttpResponse('sai dữ liệu')
        if request.user.has_perm('Login.add_post'):
            f.save()
            return HttpResponse('đã lưu')
        else: 
            return HttpResponse('không có quyền')