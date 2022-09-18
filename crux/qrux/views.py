from django.http import HttpResponse
from django.shortcuts import render

from .models import Contact


# Create your views here.


def home(request):
    # return HttpResponse("Home page" "|" "|" "Home all information is available here")
    return render(request, 'home.html')


def about(request):
    # return HttpResponse('About page')
    return render(request, 'about.html')


def project(request):
    context = {
        'name': 'skippy', 'job': 'manager', 'place': 'EPK'
    }
    # return HttpResponse('Projects page')
    return render(request, 'project.html', context)


def search(request, blog=None):
    blog = blog.objects.all()
    context = {'blog': blog}
    return render(request, 'search.html', context)


def blogpost(request, slug):
    return HttpResponse(request, f"You are visiting {slug}")


def blog(request):
    return render(request, 'blogpost.html')


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        ins = Contact(name=name, email=email, phone=phone, desc=desc)
        ins.save()
        print("The data has been writen to the db")
    # return HttpResponse('Contact page')
    return render(request, 'contact.html')


def bloghome(request):
    return render(request, 'bloghome.html')
