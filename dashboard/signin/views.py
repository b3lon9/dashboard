from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from signin.models import User

# Create your views here.
def login_page(request):
    # return HttpResponse("OK")
    user_list = User.objects.all()
    context = {'user_list':user_list}
    return render(request, 'signin/login_page.html', context)

def detail(request, user_id):
    # user = User.objects.get(id=user_id)

    # not found 404
    user = get_object_or_404(User, pk=user_id)
    context = { 'user' : user}
    return render(request, 'signin/detail.html', context)

def create(request):
    new_user = request.POST.get()
    print('create')
    return HttpResponse("create")

# user register
def register(reqeust):
    return HttpResponse("register")