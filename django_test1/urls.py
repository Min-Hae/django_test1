"""django_test1 URL Configuration

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
from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('hello', views.helloFunc), # hello라는 요청이 왔을 때 helloFunc가 실행된다.
    # 127.0.0.1/hello_temp를 주소창에 입력하면 views.py안의 hello_temp_Func함수가 실행됨.
    path('hello_temp', views.hello_temp_Func), 
    path('world', views.worldFunc),
]
