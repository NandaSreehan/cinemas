from django.shortcuts import render
from django.http import HttpResponse

def func1(request):
    d={
        'place':'vizag'
    }
    return render(request,'index.html',d)


def func2(request):
    d1={'name':'appalaraju','age':18,'status':'Eligible'}
    return render(request,'vote.html',d1)

def func3(request):
    d2={'movies':[
        {'name':'varsham','imdb':4,'writer':"nanda",'year':2004,'director':'Naveen'},
        {'name':'Salaar','imdb':3,'writer':"raju",'year':2024,'director':'Prashanth Neelu'},
        {'name':'Billa','imdb':8,'writer':"srinivas",'year':2008,'director':'yeshwanth'},
        {'name':'varsham','imdb':4,'writer':"nanda",'year':2004,'director':'Naveen'},
        {'name':'dress','imdb':4,'writer':"reddy",'year':2004,'director':'Naveen'},
        {'name':'bag','imdb':4,'writer':"redd",'year':2004,'director':'Naveen'},
        {'name':'bottle','imdb':4,'writer':"nanda",'year':2004,'director':'Naveen'},

        ]}
    return render(request,'table.html',d2)