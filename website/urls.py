"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from signup.views import signaction
from login.views import loginaction
from forgotpwd.views import forgotaction
from about.views import aboutaction
from home.views import homeaction
from contact.views import contactaction
from feedback.views import feedaction
from movies.views import movieaction
from feed_submit.views import feed_submitaction
from the_boys.views import boysaction
from money_heist.views import heistaction
from barbie.views import barbieaction
from oppenheimer.views import oppenheimeraction
from red_white_and_royal_blue.views import blueaction
from all_of_us_are_dead.views import deadaction
from kota_factory.views import factoryaction
from ginny_and_georgia.views import georgiaaction
from kai_po_che.views import cheaction
from uncharted.views import unchartedaction
from the_white_lotus.views import lotusaction
from kabir_singh.views import singhaction
from a_thursday.views import thursdayaction
from heartstopper.views import heartstopperaction
from spiderman.views import spidermanaction

urlpatterns = [
    path('', lambda request: redirect('home/')),
    path('admin/', admin.site.urls),
    path('signup/', signaction),
    path('login/', loginaction),
    path('forgotpwd/', forgotaction),
    path('about/', aboutaction),
    path('home/', homeaction),
    path('contact/', contactaction),
    path('feedback/', feedaction),
    path('movies/', movieaction),
    path('feed_submit/', feed_submitaction),
    path('movies/the boys.html', boysaction),
    path('movies/money heist.html', heistaction),
    path('movies/ginny and georgia.html', georgiaaction),
    path('movies/uncharted.html', unchartedaction),
    path('movies/a thursday.html', thursdayaction),
    path('movies/kai po che.html', cheaction),
    path('movies/kabir singh.html', singhaction),
    path('movies/heartstopper.html', heartstopperaction),
    path('movies/the white lotus.html', lotusaction),
    path('movies/spiderman.html', spidermanaction),
    path('movies/kota factory.html', factoryaction),
    path('movies/all of us are dead.html', deadaction),
    path('movies/barbie.html', barbieaction),
    path('movies/oppenheimer.html', oppenheimeraction),
    path('movies/red white and royal blue.html', blueaction),
]
