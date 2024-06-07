from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import RegistrationFord
from django.contrib import admin
from django.urls import include, path
from django.urls import path
from .views import register 
from django.db import models
from django import forms
from .models import Event
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

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'users',
        'USER': 'root',
        'PASSWORD': '1243',
        'HOST': '30.30.30.30',
        'PORT': '3306',
    }
}

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.name

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'ledger/register.html', {'form': form})
    else:
        form = RegistrationForm()
        return render(request, 'ledger/register.html', {'form': form})

urlpatterns = [
    path('register/', register, name='register'),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ledger.urls')),
]
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Register</title>
# </head>
# <body>
#     <h1>Register</h1>
#     <form method="POST">
#         {% csrf_token %}
#         {{ form.as_p }}
#         <button type="submit">Register</button>
#     </form>
# </body>
# </html>
