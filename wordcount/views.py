from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request,'home.html')

def count(request):

    fulltext=request.GET['fulltext']

    wordlist1 = fulltext.split(' ')
    wordlist=[]
    for word in wordlist1:
        if word!="":
            wordlist.append(word)
        print(wordlist)
    error=""
    if wordlist==[""]:
        error="Text is empty"

    worddictionary={}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
    sorteddictionary = sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)

    return render(request,"count.html",{'fulltext':fulltext,'count':len(wordlist),'sorteddictionary':sorteddictionary,'error':error})

def about(request):
    return render(request,'about.html')
