from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('인덱스 요청 처리')

def helloFunc(request):
    msg = 'Hello'
    ss = '<html><body>Nice %s</body></html>'%(msg)
    return HttpResponse(ss)

def hello_temp_Func(request):
    msg = '홍길동'
    return render(request, 'show.html', {'name':msg}) # name이라는 이름의 키로 msg 값을 가져감.

def worldFunc(request):
    return render(request, 'disp.html')