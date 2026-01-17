"""
URL configuration for yukko_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.contrib.auth.models import User
from django.http import HttpResponse

def create_admin(request):
    # Защита: только если на Render и нет пользователей
    if '.onrender.com' in request.get_host() and not User.objects.exists():
        User.objects.create_superuser(
            username='yukkoGod',
            email='ivansila2707@mail.ru',
            password='god2707'  # ПОМЕНЯЙ ПАРОЛЬ!
        )
        return HttpResponse('<h1>Admin created!</h1><p>Username: admin<br>Password: admin123</p>')
    else:
        return HttpResponse('<h1>Admin already exists or not on Render</h1>')

urlpatterns = [
    path('create-admin/', create_admin),  # ДОБАВЬ ЭТУ СТРОЧКУ
    path('admin/', admin.site.urls),
    path("", include('yukko_blog.app.urls')),
]