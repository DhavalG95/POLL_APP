from django.shortcuts import render , redirect
from .models import *
from .forms import *
from django.http import HttpResponse


# Create your views here.
def home(request):
    polls = Poll.objects.all().values()
    return render(request,'home.html',context={'polls' : polls})

def create(request):
    
    if request.method == 'POST':
        form = CreatePollForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return redirect ('home')
    
    else:
        form = CreatePollForm()
        
    return render(request,'create.html',context={'form':form})

def vote(request,poll_id):
    polls = Poll.objects.get(id=poll_id)
    if request.method == "POST":
        selected_option = request.POST['poll']
        if selected_option == "option1":
            polls.option_one_count += 1
        elif selected_option == "option2":
            polls.option_two_count += 1
        elif selected_option == "option3":
            polls.option_three_count += 1
        else:
            return HttpResponse(400 , 'Invalid Form')

        polls.save()

        return redirect ('results' ,polls.id)
    return render(request,'vote.html',context={'polls':polls})

def results(request,poll_id):
    pollresult = Poll.objects.get(id=poll_id)
    return render(request,'results.html',context={'pollresult':pollresult})

