from django.http import HttpResponse
from django.shortcuts import render, redirect
from bbs.models import bbs_list


# Create your views here.

def start(request):
    return HttpResponse(
        '<h1>Hello, this is homepage.</h1><br><hr color="red">' +
        "<h1><a href=admin>Admin Page</a></h1><br><br>" +
        '<h1><a href=bbs>bbs page</a></h1>'
    )


def index(request):
    return HttpResponse(
        "<h1><a href=register>Create bbs</a></h1><br><br>")


def create(request):
    data = request.POST
    title2 = data.get('title')
    name2 = data.get('name')
    email2 = data.get('email')
    contents2 = data.get('contents')
    b_data = bbs_list(title=title2, name=name2, email=email2,
                        contents=contents2, createDate='2021-06-10')
    b_data.save()
    return redirect('/bbs/show_list')


def register(request):
    # data = request.POST
    # 입력값을 딕셔너리 형태로 넣어줌
    # context = {"data": data}
    return render(request, "bbs/register.html")


def delete(request, id):
    data = bbs_list.objects.get(id=id)
    data.delete()
    return redirect('/bbs/show_list')


# Get 방식으로 파라메터 id 값을 넘겨 받음
# id를 검색 해서 보여주는 역할
# member/urls.py에서 입려한 views의 함수를 찾아서 실행
def update(request, id):
    # request 객체가 member/페이지의 input에서 입력한 정보를 받음

    data = bbs_list.objects.get(id=id)
    context = {"data": data}
    # update.html로 context 값(id)를 넘긴다.
    # render(입력값이 할당된 변수, "클라이언트가 요청한 정보를 보여줄 페이지 경로")
    return render(request, 'bbs/update.html', context)


# Post 방식으로 update.html에서 수정된 값들을 전송
def update2(request):
    data = request.POST
    # 전송받은 data의 id를 one 변수에 저장 후
    # member의 test db에 저장
    one = bbs_list.objects.get(id=data.get('id'))
    one.title = data.get('title')
    one.name = data.get('name')
    one.email = data.get('email')
    one.contents = data.get('contents')
    one.save()
    return redirect('/bbs/show_list')

def show_list(request):
    # name 역순으로 order_by 묶어서 보여줌
    bbs_list1 = bbs_list.objects.order_by('-id')[:10]
    context = {'bbs_list': bbs_list1}
    return render(request, 'bbs/show_list.html', context)

def one(request, id):  # request 객체가 member/페이지의 input에서 입력한 정보를 받음
    data = bbs_list.objects.get(id=id)
    context = {"data": data}
    # update.html로 context 값(id)를 넘긴다.
    # render(입력값이 할당된 변수, "클라이언트가 요청한 정보를 보여줄 페이지 경로")
    return render(request, 'bbs/one.html', context)
