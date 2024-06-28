"""
URL configuration for gestionUsarios project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from packages.users.views import (
    CreaterUserView, LoginUser, LogoutView, UpdatePasswordView, ValidateCodeView
)

app_name = 'users'

urlpatterns = [
    path('nuevoUsuario/', CreaterUserView.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='salir'),
    path('update/', UpdatePasswordView.as_view(), name='update'),
    path('user-verification/<int:pk>', ValidateCodeView.as_view(), name='user_verification'),
]
