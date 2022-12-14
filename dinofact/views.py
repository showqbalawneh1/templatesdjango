from django.shortcuts import render
from datetime import datetime


# Create your views here.


def show (request,word):
    
    data = {
        'dinosaurs':[
            "tyttyryyy",
            "statstsd",
            "rtsidtst",
            "Trisdus",
        ],
        "now": datetime.now(),
    }
    path ='show_dino/'+word+'.html'
    return render(request,path,data)