from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def signup(request):
    return render(request,"signup.html")


from django.shortcuts import render, redirect
from .forms import EventForm

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_event')
    else:
        form = EventForm()
    return render(request, 'ledger/add_event.html', {'form': form})
