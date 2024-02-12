from django.shortcuts import render,get_object_or_404,redirect
# from rest_framework.generics import ListCreateAPIView
# from .serializers import *
from .models import *
from .form import *


# Create your views here.
# class PostTemp(ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers


def index(req):
    data = {
        'all': ToDo.objects.all(),
        'coplated': ToDo.objects.all().filter(complate=True),
        'active': ToDo.objects.all().filter(complate=False),
        'count': len(ToDo.objects.all())
    }
    return render(req,'index.html',data)


def check(req,pk):
    el = ToDo.objects.get(pk=pk)
    el.complate = (False if el.complate else True)
    el.save()

    return redirect('home')

def delete(req,pk):
    el = ToDo.objects.get(pk=pk)
    el.delete()

    return redirect('home')


def add(req):
    form = AddForm()
    if req.method == 'POST':
        form = AddForm(req.POST)
        if form.is_valid():
            form.save()

            form = AddForm()

            return redirect('home')
    else:
        form = AddForm()    
    data = {
        'form': form
    }
    return render(req,'add.html',data)


def edit(req,pk):
    form = AddForm()
    if req.method == 'POST':
        form = AddForm(req.POST,instance=get_object_or_404(ToDo,pk=pk))
        if form.is_valid():
            form.save()

            form = AddForm()

            return redirect('home')
    else:
        form = AddForm(instance=get_object_or_404(ToDo,pk=pk))    
    data = {
        'form': form
    }
    return render(req,'add.html',data)


def info(req,pk):

    return render(req,'info.html',{"todo":get_object_or_404(ToDo,pk=pk)})