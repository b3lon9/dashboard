from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.
def login(request):
    # request.POST.get() --> id, pw
    if request.method == 'POST':
        pass
    else:
        # get
        pass
    return render(request, 'login/login.html')