from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from mod.models import *

# Create your views here.


def index(request):
	return render(request, 'index/index.html')

def results(request):
	if request.method == 'POST':
		query = request.POST.get("query")
		results = Item.objects.filter(name__icontains=query).filter(description__icontains=query)
		context = {"results": results}
		return render(request, 'index/results.html', context)
	else:
		return render(request, 'index/index.html')

def details(request, item_id):
	if item_id:
		item = Item.objects.filter(id=item_id)
		if item.exists():
			context = {"item": Item.objects.get(id=item_id)}
			print(context)
			return render(request, 'index/details.html', context)
	return render(request, 'index/index.html')