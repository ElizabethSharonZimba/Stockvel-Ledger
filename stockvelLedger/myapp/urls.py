from django.urls import path
from . import views


urlpatterns=[
    path("",views.home,name="home"),
    path("about/",views.about,name="about"),
    path("signup/",views.signup,name="signup"),
    path("signin/",views.signup,name="signin")

]

from django.urls import path
from .views import add_event

urlpatterns = [
    path('add_event/', add_event, name='add_event'),
]
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ledger.urls')),
]
