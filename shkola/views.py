from django.http import HttpResponse
from django.shortcuts import render
from . import forms
from .models import Uroki

# Create your views here.
def start(request):
    context = {
        "greeting": "Здравствуй, гость",
    }
    return render(request, "start.html", context)

def student(request):

    all_lessons = Uroki.objects.all()

    context = {
        "greeting": "Здравствуй, ученик",
        "imya": "Василий",
        "uroki": all_lessons
    }
    return render(request, "student.html", context)

def uchitel(request):

    form_for_new_urok = forms.UrokiForm

    context = {
        'greeting': "Здравствуйте, Василий Петрович!",
        'urokForm': form_for_new_urok,
    }
    return render(request, "uchitel.html", context)

def add_urok(request):
    form = forms.UrokiForm(request.POST)
    result = "Урок успешно добавлен %s" %request.path
    if request.method == 'POST':
        if form.is_valid():
            data = form.cleaned_data
            form.save()
            print(data['nazvanie_predmeta'])

            return render(request, "add_urok.html")