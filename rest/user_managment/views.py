from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import render, redirect
from .models import User
from .forms import new, edit


def all_users(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'user_managment/index.html', context)


def create_user(request):
    if request.method == 'GET':
        context = {
            'form': new(),
        }
        return render(request, 'user_managment/new.html', context)
    elif request.method == 'POST':
        User.objects.create(name=request.POST['name'], email=request.POST['email'])
        return redirect(reverse('index'))

def edit_user(request, user_id):
    context = {
        'form': edit(),
        'id': user_id,
    }
    return render(request, 'user_managment/edit.html', context)


def update(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.POST['id'])
        user.name = request.POST['name']
        user.email = request.POST['email']
        user.save()
        return redirect(
            reverse('show_user', kwargs={'user_id': int(request.POST['id'])})
            )

def show_user(request, user_id):
    context = {
        'account': User.objects.get(id=user_id)
    }
    return render(request, 'user_managment/inspect.html', context)


def destroy_user(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect(reverse('index'))
