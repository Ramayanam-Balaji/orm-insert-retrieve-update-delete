from django.shortcuts import render

# Create your views here.
from app1.models import *
def display_topics(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    return render(request,'display_topics.html',d)
def display_Webpages(request):
    Webpages=Webpage.objects.all()
    d1={'Webpages':Webpages}
    return render(request,'display_Webpages.html',d1)
def display_AccessRecordss(request):
    AccessRecordss=AccessRecords.objects.all()
    d2={'AccessRecordss':AccessRecordss}
    return render(request,'display_AccessRecordss.html',d2)