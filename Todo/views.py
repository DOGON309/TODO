from django.shortcuts import render, redirect
from .models import TodoModel
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def loginview(request):
	params = {
		'title': 'ログイン',
		'form': Loginform,
		'message': '',
	}
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request, user)
			return redirect('/')
		else:
			params['message'] = 'ユーザー名、またはパスワードが間違っています'
			return render(request, 'Todo/login.html', params)
	return render(request, 'Todo/login.html', params)

def logoutview(request):
	logout(request)
	return redirect('/login')

@login_required(login_url='/login')
def indexview(request):
	params = {
		'title': 'APP',
		'form': Indexform,
		'contents': '',
	}
	if request.method == 'POST':
		todo = request.POST['todo']
		select = request.POST['choice']
		todomodel = TodoModel()
		todomodel.content = todo
		todomodel.select = select
		todomodel.save()
		params['contents'] = TodoModel.objects.all()
		return redirect('/')
	else:
		params['contents'] = TodoModel.objects.all()
		return render(request, 'Todo/index.html', params)

def deleteview(request, id):
	TodoModel.objects.get(pk = id).delete()
	return redirect('/')