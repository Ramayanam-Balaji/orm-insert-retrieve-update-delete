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
    Webpages=Webpage.objects.all()
    d1={'Webpages':Webpages}
    return render(request,'display_Webpages.html',d1)
def display_AccessRecordss(request):
    AccessRecordss=AccessRecords.objects.all()
    d2={'AccessRecordss':AccessRecordss}
    return render(request,'display_AccessRecordss.html',d2)
def update_Webpages(request):
    #Webpage.objects.filter(Name='virat').update(url='http://virat.com')
    Webpage.objects.update_or_create(Name='dhoni',defaults={'url':'https://dhoni.com'})
    Wto=Webpage.objects.all()
    d1={'Webpages':Wto}
    return render(request,'display_Webpages.html',d1)
def delete_Webpages(request):
    Webpage.objects.all().delete()
    Wto=Webpage.objects.all()
    d1={'Webpages':Wto}
    return render(request,'display_Webpages.html',d1)