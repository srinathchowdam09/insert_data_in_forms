from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.


def topic(request):
    if request.method =="POST":
         tn=request.POST['topic']
         T=Topic.objects.get_or_create(topic_name=tn)[0]
         T.save()
         return HttpResponse('insert topic is done')

       
    return render(request,'topic.html')

def webpage(request):
    if request.method=="POST":
        tn=request.POST['webpage']
        W=Webpage.objects.get_or_create(name=tn)[0]
        W.save()
        return HttpResponse('insert name is done')

    return render(request,'webpage.html')
