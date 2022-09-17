from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from .models import Question, FormQuestion
# Create your views here.

def show_page(request):
    if request.method != 'POST':
        return render(request, 'app1/index.html')

    print('salam')

    form = FormQuestion(request.POST)
    print(form.fields)
    if form.is_valid():
        q = form.save()
        q.save()
        print(q)
    else:
        print(form.errors)
        print("vaaaaay")
    return render(request, 'app1/index.html')
