"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from mainapp import views as views

urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^$', views.home, name='home' ),

    # sign up view
    url(r'^signup/$', views.signup, name='signup' ),

    # posts login request
    path('login', views.log_in, name="loggedin"),

    path('new_password', views.new_password, name="new_password"),

    # register
    url(r'^register_user/$', views.register_new_user, name='regster_new_user' ),

    # dashboard
    url(r'^dashboard/$', views.dashboard, name='dashboard' ),

    url(r'^logout/$', views.logout, name='logout'),
]
