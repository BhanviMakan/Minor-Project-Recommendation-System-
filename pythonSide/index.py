from django.shortcuts import render
from subprocess import run,PIPE
import sys
import requests

def output(request):
    data = requests.get("https://www.google.com/")
    print(data.text)
    data=data.text
    return render(request,'songs.html',{'data':data})

def output_1(request):
    data = requests.get("https://www.google.com/")
    print(data.text)
    data=data.text
    return render(request,'Movies.html',{'data':data})

def output_2(request):
    data = requests.get("https://www.google.com/")
    print(data.text)
    data=data.text
    return render(request,'place.html',{'data':data})

def xyz(request):
    data = requests.get("https://www.google.com/")
    print(data.text)
    data=data.text
    return render(request,'food.html',{'data':data})


def page1(request):
    return render(request,'index.html')

def page2(request):
    return render(request,'home.html')

def page3(request):
    return render(request,'Movies.html')

def external_1(request):
    inp=request.POST.get('fname')
    out=run([sys.executable,'C:\\Users\\Bhanvi\\Desktop\\minor project\\pythonSide\\pythonSide\\movie_recommender.py',inp],shell=False,stdout=PIPE)
    print(out)
    return render(request,'Movies.html',{'data2':out.stdout})

def external(request):
    inp=request.POST.get('fname1')
    out=run([sys.executable,'C:\\Users\\Bhanvi\\Desktop\\minor project\\pythonSide\\pythonSide\\song_recommender.py',inp],shell=False,stdout=PIPE)
    print(out)
    return render(request,'songs.html',{'data1':out.stdout})

def page4(request):
    return render(request,'songs.html')


def page5(request):
    return render(request,'place.html')

def external_2(request):
    inp=request.POST.get('fname2')
    out=run([sys.executable,'C:\\Users\\Bhanvi\\Desktop\\minor project\\pythonSide\\pythonSide\\place_recommender.py',inp],shell=False,stdout=PIPE)
    print(out)
    return render(request,'place.html',{'data3':out.stdout})


def page6(request):
    return render(request,'food.html')

def external_3(request):
    inp=request.POST.get('fname3')
    out=run([sys.executable,'C:\\Users\\Bhanvi\\Desktop\\minor project\\pythonSide\\pythonSide\\food_recommender.py',inp],shell=False,stdout=PIPE)
    print(out)
    return render(request,'food.html',{'data4':out.stdout})
