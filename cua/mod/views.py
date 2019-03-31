from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import *

# Create your views here.

@staff_member_required
def index(request):
	return render(request, 'mod/index.html')

@staff_member_required
def logout_view(request):
	if request.user.is_authenticated:
		logout(request)
	return HttpResponseRedirect(reverse('index'))

@staff_member_required
def input_view(request):
	context = {'input':Item_Request.objects.all()}
	return render(request, 'mod/input.html', context)

@staff_member_required
def tags_view(request):
	context = {'input':Tags_Request.objects.all()}
	return render(request, 'mod/tags.html', context)


@staff_member_required
def details(request, item_id):
	if item_id:
		item = Item_Request.objects.filter(id=item_id)
		if item.exists():
			context = {"item": item.get()}
			return render(request, 'mod/details.html', context)
	return HttpResponseRedirect(reverse('index'))