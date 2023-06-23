from django.shortcuts import render
from django.db.models.functions import Length
# Create your views here.
from app1.models import *
def display_topics(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    return render(request,'display_topics.html',d)
def display_Webpages(request):
    Webpages=Webpage.objects.all()
    #Webpages=Webpage.objects.get(Webpage)
    Webpages=Webpage.objects.filter(Name='virat')
    Webpages=Webpage.objects.exclude(Name='virat')
    Webpages=Webpage.objects.all().order_by('Name')
    Webpages=Webpage.objects.all().order_by('-Name')
    Webpages=Webpage.objects.all().order_by(Length('Name'))
    Webpages=Webpage.objects.all()[1:4]
    Webpages=Webpage.objects.all()[::-1]

    
    
    
    



    d1={'Webpages':Webpages}
    return render(request,'display_Webpages.html',d1)
def display_AccessRecordss(request):
    AccessRecordss=AccessRecords.objects.all()
    d2={'AccessRecordss':AccessRecordss}
    return render(request,'display_AccessRecordss.html',d2)