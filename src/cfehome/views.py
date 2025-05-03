from django.http import HttpResponse,HttpRequest
import pathlib
from django.shortcuts import render
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent


def home_page(request,*args,**kwargs):
    qs = PageVisit.objects.all()
    qs_home = PageVisit.objects.filter(path=request.path )
    my_title = "My Page"
    my_context = {
        "page_title":my_title,
        "page_visits_count":qs_home.count(),
        "total_visits_count":qs.count()
    }
    html_template="home.html"
    PageVisit.objects.create(path=request.path)
    return render(request,html_template,my_context)