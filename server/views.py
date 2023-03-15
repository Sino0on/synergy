from django.shortcuts import render
from .models import *


def home(request):
    grants = Grant.objects.all()
    programs = Program.objects.all()
    feedbacks = Feedback.objects.all()
    return render(request, 'index.html', {'programs': programs, 'grants': grants, 'feedbacks': feedbacks})


def about(request):
    grants = Grant.objects.all()
    programs = Program.objects.all()
    feedbacks = Feedback.objects.all()
    return render(request, 'about.html', {'programs': programs, 'grants': grants, 'feedbacks': feedbacks})


def program_list(request):
    grants = Grant.objects.all()
    programs = Program.objects.all()
    feedbacks = Feedback.objects.all()
    return render(request, 'programs.html', {'programs': programs, 'grants': grants, 'feedbacks': feedbacks})


def about(request):
    grants = Grant.objects.all()
    programs = Program.objects.all()
    feedbacks = Feedback.objects.all()
    return render(request, 'about.html', {'programs': programs, 'grants': grants, 'feedbacks': feedbacks})


def grant_list(request):
    grants = Grant.objects.all()
    programs = Program.objects.all()
    feedbacks = Feedback.objects.all()
    return render(request, 'grants.html', {'programs': programs, 'grants': grants, 'feedbacks': feedbacks})


def news_list(request):
    grants = Grant.objects.all()
    programs = Program.objects.all()
    feedbacks = Feedback.objects.all()
    return render(request, 'news.html', {'programs': programs, 'grants': grants, 'feedbacks': feedbacks})


def contact(request):
    grants = Grant.objects.all()
    programs = Program.objects.all()
    feedbacks = Feedback.objects.all()
    return render(request, 'contact.html', {'programs': programs, 'grants': grants, 'feedbacks': feedbacks})


def program_detail(request, pk):
    grants = Grant.objects.all()
    programs = Program.objects.all()
    program = Program.objects.get(id=pk)
    feedbacks = Feedback.objects.all()
    return render(request, 'program_detail.html', {'programs': programs, 'grants': grants, 'feedbacks': feedbacks, 'program': program})


def grant_detail(request, pk):
    grants = Grant.objects.all()
    programs = Program.objects.all()
    grant = Grant.objects.get(id=pk)
    feedbacks = Feedback.objects.all()
    return render(request, 'grant_detail.html', {'programs': programs, 'grants': grants, 'feedbacks': feedbacks, 'grant': grant})
