from django.http import HttpResponse
from django.shortcuts import render



def homepage(request):
    return render(request , 'homepage.html')

def Count(request):
    fulltext=request.GET["fulltext"]
    wordslist=fulltext.split()
    count=len(wordslist)
    print(wordslist)
    worddic={}
    for word in wordslist:
        if(word in worddic.keys()):
            worddic[word]+=1
        else:
            worddic[word]=1
    print(worddic)
    
    return render(request , 'Count.html' , {'fulltext':fulltext,'wordcount':count , 'worddic':worddic.items()})


def About(request):
    return render(request , 'About.html')