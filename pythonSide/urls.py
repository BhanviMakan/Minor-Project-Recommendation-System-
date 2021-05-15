"""pythonSide URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import index
urlpatterns = [
    path('',index.page1,name='page1'),
    path('home',index.page2,name='page2'),

    path('output_1',index.output_1),
    url('external_1',index.external_1),
    path('Movies',index.page3,name='page3'),

    path('output',index.output),
    url('external',index.external),
    path('songs',index.page4,name='page4'),

    path('output_2',index.output_2),
    url('jga',index.external_2),
    path('place',index.page5,name='page5'),

    path('xyz',index.xyz),
    url('kha',index.external_3),
    path('food',index.page6,name='page6')

]
