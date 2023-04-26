from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from app.models import *
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse('Topic insertion is done Successfully')

    return render(request,'insertion_topic.html')


def insert_webpage(request):
    lot=Topic.objects.all()
    d={'topics':lot}
    if request.method=='POST':
          topic=request.POST['topic']
          name=request.POST['name']
          url=request.POST['url']
          T1=Topic.objects.get(topic_name=topic)
          WO=Webpage.objects.get_or_create(topic_name=T1,name=name,url=url) [0]
          WO.save()
          return HttpResponse('webpage insertion done suceesfully')
     
    return render(request,'insertion_webpage.html',d)

def insert_Accessrecord(request):
     low=Webpage.objects.all()
     d={'webpages':low}
     if request.method=='POST':
          webpage=request.POST['webpage']
          author=request.POST['author']
          date=request.POST['date']
          WO=Webpage.objects.get(name=webpage)
          AO=AccessRecord.objects.get_or_create(name=WO,author=author,date=date) [0]
          AO.save()
          return HttpResponse('accessrecord insertion done successfully')
     return render(request,'insertion_Accessrecord.html',d)


def retrieve_data(request):
     LTO=Topic.objects.all()
     d={'topics':LTO}
     if request.method=='POST':
        td=request.POST.getlist('topic')
        print(td) 
        webqueryset=Webpage.objects.none()

        for i in td:
            webqueryset=webqueryset|Webpage.objects.filter(topic_name=i)
            d1={'webpages':webqueryset}
        return render(request,'display_webpage.html',d1)
     return render(request,'retrieve_data.html',d)

def checkbox(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}
    return render(request,'checkbox.html',d)


def radio(request):
    lto=Topic.objects.all()
    d={'topics':lto}
    return render(request,'radio.html',d)

def update_webpage(request):
    low=Webpage.objects.all()
    d={'webpages':low}
    if request.method=='POST':
        w=request.POST.getlist('webpage')
        new=request.POST['new']
        for i in w:
            Webpage.objects.filter(name=i).update(url=new)
        d1={'webpages':Webpage.objects.all()}
        return render(request,'display_webpage.html',d1)
    return render(request,'update_webpage.html',d)

def delete_webpage(request):
    low=Webpage.objects.all()
    d={'webpages':low}
    if request.method=='POST':
         w=request.POST.getlist('webpage')
         for i in w:
            Webpage.objects.filter(name=i).delete()
         d1={'webpages':Webpage.objects.all()}
         return render(request,'display_webpage.html',d1)

    return render(request,'delete_webpage.html',d)