from django.http import HttpResponse
from django.shortcuts import render
import os


file_path=os.path.abspath(__file__)
pro4_dir_path=os.path.dirname(file_path)
dir_path=os.path.dirname(pro4_dir_path)


def index(request):
    return HttpResponse("<marquee direction=\"right\"><h1>goog morning alllll</h1></marquee>")


def html_respo(request):
    file_addr=os.path.join(dir_path,"sample.html")
    fp=open(file_addr,"r")
    data=fp.read()
    return HttpResponse(data)
    
  
