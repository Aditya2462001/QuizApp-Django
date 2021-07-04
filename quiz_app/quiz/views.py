from django.db import connections
from django.shortcuts import render,HttpResponse ,redirect
from .models import *


# Create your views here.

def subject(request):
    subject = Subject.objects.all()
    return render(request,'main.html',{'subjects':subject})


def questions(request,pk):
    subject = Subject.objects.get(id = pk)
    questions = Question.objects.all()
    questions = questions.filter(subject = subject)

    datas = []
    if request.method == "POST":
        for que in questions:
            data = [] 
            data.append(request.POST.get(str(que.id)))
            if data is not None:
                data.append(que.id)
            datas.append(data)
    return render(request,'question.html',{'questions':questions,"subject":subject,'total':len(questions)})



def result(request):
    all_data = []
    correct = 0
    wrong = 0
    not_attempt = 0
    questions = Question.objects.all()
    if request.method == 'POST':
        subject = Subject.objects.get(name = request.POST.get('subject'))
        questions = questions.filter(subject = subject)
        print(subject)
        for que in questions:
            data = []
            ans = request.POST.get(str(que.id))
            if ans == que.answer :
                data.append('Yes')
                data.append(que.id)
                correct += 1
            else:
                if ans is None:
                    data.append('Not')
                    data.append(que.id)
                    not_attempt += 1
                else:
                    data.append('No')
                    data.append(que.id)
                    wrong += 1
            data.append(ans)
            all_data.append(data)

    context = {
        'all_data':all_data,
        'questions' : questions,
        'correct': correct,
        'wrong' : wrong,
        'not_attempt':not_attempt,
        'subject' : subject
    }

    return render(request,'result.html',context)


def about(request):
    return render(request,'about.html')
                


