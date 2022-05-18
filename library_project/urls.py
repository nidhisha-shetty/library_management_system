"""library_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from library_app.views import *

urlpatterns = [
    path('', base_home_view),
    path('home/', home_view),
    path('signup/', signup_view),
    path('login/', auth_views.LoginView.as_view(), {'template_name': 'record.html'}),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('user_add', add_view),
    path('create/', create_view),
    path('edit/<int:id>', edit_view),
    path('view/<int:id>', view_view),
    path('delete/<int:id>', delete_view),
    path('edit_list/', edit_list_view),
    path('view_list/', view_list_view),
    path('delete_list/', delete_list_view)
]