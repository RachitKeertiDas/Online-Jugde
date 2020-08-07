from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from background_task import background
import os
from .models import *
from collections import deque
# Create your views here.

@background(schedule=0)
def run(sub_id):
    submission = Submission.objects.get(pk=sub_id)
    ques = submission.ques
    testcases = ques.testcases.all()
    with open(f'{sub_id}.cpp','w') as f:
        f.write(submission.code)
    x = os.system(f'g++ {sub_id}.cpp -o {sub_id}')
    for testcase in testcases:
        os.system(f'echo {testcase.testcase} | ./{sub_id} > {sub_id}.out')
        with open(f'{sub_id}.out','r') as f:
            x = f.read()
        t = Output(submission=submission, output=x)
        t.save()

def index(request):
    questions = Question.objects.all()
    context = { "questions":questions }
    return render(request, 'practice/index.html',context)

def ques(request, ques_id):
    question = Question.objects.get(pk=ques_id)
    context = { "question":question, "submissions":question.submissions.all() }
    return render(request, 'practice/ques.html', context)

def addques(request):
    if request.method == "POST":
        x = request.POST
        f = Question(name=x["name"], statement=x["statement"])
        f.save()
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'practice/addques.html')

def submit(request, ques_id):
    if request.method == "POST":
        x = request.POST
        ques = Question.objects.get(pk=ques_id)
        f = Submission(ques=ques, code=x["code"], lang=x["lang"])
        f.save()
        run(f.id)
        return HttpResponseRedirect(reverse('index'))

    lang = ['C++','C','Python']
    context = { "ques_id": ques_id, "lang":lang }
    return render(request, 'practice/submit.html', context)

def submission(request, sub_id):
    x = Submission.objects.get(pk=sub_id)
    q = x.ques
    context = { "outputs": x.outputs.all(), "tcs":q.testcases }
    return render(request, 'practice/submission.html', context)