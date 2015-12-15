from django.shortcuts import render
from django.http import Http404, HttpResponse 
from django.template import Context 
from django.template.loader import get_template 

 
def current_datetime(request): 
    try:
        f = open("file.txt","r")
        lines = f.readlines()
        words= {}
        for line in lines:
            line = line.split(" ")
            for word in line:
                if word not in words:
                    words[word]=1
                else:
                    words[word]+=1

        t = get_template('kerime.html') 
        html = t.render(Context({'words': words})) 
        return HttpResponse(html)
    except:
        Http404()