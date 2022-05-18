from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import Libraryform
from django.contrib import messages
from .models import Lib

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=email, password=raw_password)
            login(request, user)
            return redirect('/home')
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {'form': form})

def add_view(request):
	form=Libraryform(request.POST or None)
	if form.is_valid():
		form.save()
		form=Libraryform()
		messages.info(request, "User details added successfully!")
	context={  
		'forming':form
		}
	return render(request, "user_create.html", context)

def create_view(request):
	form=Libraryform(request.POST or None, request.FILES or None)
	if form.is_valid():
		messages.info(request, "Book details saved!")
		form.save()
		form=Libraryform()

	context={
		'context_form': form	
	}
	return render(request, 'create.html', context)


def edit_view(request, id):
	obj=Lib.objects.get(id=id)
	form=Libraryform(request.POST or None, request.FILES or None, instance=obj)
	if form.is_valid():
		form.save()
		form=Libraryform()
	context={
	'context_form': form
	}
	return render(request, 'edit.html', context)


def view_view(request, id):
	obj=Lib.objects.get(id=id)
	context={
	'context_obj': obj
	}
	return render(request, 'view.html', context)

def delete_view(request, id):
	obj=Lib.objects.get(id=id)
	if request.method=='POST':
		obj.delete()
		return redirect("/home")
	context={
	'context_obj': obj
	}
	return render(request, 'delete.html', context)

def edit_list_view(request):
	queryset=Lib.objects.all()
	context={
	'context_qs': queryset
	}
	return render(request, 'edit_list_view.html', context)


def view_list_view(request):
	queryset=Lib.objects.all()
	context={
	'context_qs': queryset
	}
	return render(request, 'view_list_view.html', context)

def delete_list_view(request):
	queryset=Lib.objects.all()
	context={
	'context_qs': queryset
	}
	return render(request, "delete_list_view.html", context)

def  home_view(request):
    return render(request, "home.html", {})

def  base_home_view(request):
    return render(request, "base_home.html", {})
