"""
URL configuration for core project.

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
from django.urls import path
from uni_app.views import kurs_list, professor_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kurse/', kurs_list, name='kurs_list'), #uni_app içindeki urls.py'yi dahil et
    path('professoren/',professor_list, name='professor_list'), #uni_app içindeki urls.py'yi dahil et
]
