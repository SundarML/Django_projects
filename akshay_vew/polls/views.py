from django.shortcuts import render, redirect
from polls.models import Employees

# Create your views here.
def home(request):
	emp = Employees.objects.all()
	context = {'emp': emp}

	return render(request, 'home.html', context)

def add(request):
	if request.method == "POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		address = request.POST.get('address')
		phone = request.POST.get('phone')

		wrkrs = Employees(
			name = name,
			email = email,
			address = address,
			phone = phone)
		wrkrs.save()
		return redirect('home')
	return render(request, 'home.html')

def edit(request):
	emp = Employees.objects.all()
	context = {'emp': emp}
	return redirect(request, 'home.html', context)


def update(request, id):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		address = request.POST.get('address')
		phone = request.POST.get('phone')

		lbr = Employees(
			id = id,
			name = name,
			email = email,
			address = address,
			phone = phone
			)
		lbr.save()
		return redirect('home')
	return redirect(request, 'home.html')


def about(request):
	return render(request, 'about.html', {})

def contact(request):
	return render(request, 'contact.html')
