from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

# User ID : 회원으로 이해하면 됨
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from login import models

# Create your views here.
# 대시보드 메인페이지
def index(request):
    # main dashboard page
    # context = {:}
    return render(request, 'main/index.html')