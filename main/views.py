from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from community.models import City
from django.db.models import Sum
# User ID : 회원으로 이해하면 됨
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from login import models
from django.http import JsonResponse
import json
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.
# 대시보드 메인페이지
def index(request):
    city = City.objects.values()
    city_json = json.dumps(list(city), cls=DjangoJSONEncoder)
    context = {
    #html로 보내는 필드명을 ''(따옴표)안에 넣어주면 됩니다.
    'city_json2': city_json,
    }
    print(city_json)
    
    # main dashboard page
    # context = {:}
    list2 = []
    for i in range(10):
        list2.append(i)
    print(list2)
    return render(request, 'main/base.html',context)
    # return render(request, 'dashboard/index.html',)