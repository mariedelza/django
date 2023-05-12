from django.shortcuts import render,redirect
from django.views.generic import ListView,CreateView
from .models import CreateBlog
from django.contrib.auth import authenticate
from django.contrib import messages
from .models import Contact
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


def article_detail(request, article_id):
    article = get_object_or_404(CreateBlog, pk=article_id)
    recent_articles = CreateBlog.objects.all()
    return render(request, 'article_detail.html', {'article': article, 'recent_articles': recent_articles})




class List(ListView):
    template_name = 'index.html'
    queryset = CreateBlog.objects.all()
    paginate_by =10
    
def detailView(request ,slug):
    post=CreateBlog.objects.get(slug=slug)
    
    content={
        'article':post
    }
    return render(request,'store/update.html' ,content)
    
    
    
    

def detail(request,id_article):
    article=CreateBlog.objects.get(id=id_article)
    articles_recents = article. date_added
    articles_recents = CreateBlog.objects.all().filter()
    return render(request, 'detail.html',{"article":article, "ar":articles_recents})




def search(request):
    return render(request, 'search.html')



def update(request):
    return render(request, 'update.html')


def login(request):
    return render(request, 'login.html')

def Contact(request):
    if request.method=="POST":
        contact=contact()
        name=request.POST.get("name")
        email=request.POST.get("email")
        subject=request.POST.get("subject")
        message=request.POST.get("message")
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.message=message
        contact.save()
        return HttpResponse("<h1>Merci d'avoir remplie le formulaire<h1>")
        
    return render(request , 'contact.html')


def nav(request):
    return render(request, 'nav.html')

def about(request):
    return render(request , 'about.html')

def base(request):
    return render(request, 'base.html')


def culture(request):
    return render(request, 'culture.html')


def catculture(request):
    return render(request, 'catculture.html')


def catsport(request):
    return render(request, 'catsport.html')


def category(request):
    return render(request, 'category.html')




def recherche(request):
    return render(request, 'recherche.html')

def introduction(request):
    return render(request, 'introduction.html')


def framework(request):
    return render(request, 'framework.html')


def programme(request):
    return render(request, 'programme.html')

def coder(request):
    return render(request, 'coder.html')

def traitement(request):
    return render(request, 'traitement.html')


def cultur(request):
    return render(request, 'cultur.html')


def word(request):
    return render(request, 'word.html')


def js(request):
    return render(request, 'js.html')


def ph(request):
    return render(request, 'js.html')








