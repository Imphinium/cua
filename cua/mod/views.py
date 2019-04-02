from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import logout
from django.urls import reverse
from django.http import JsonResponse, FileResponse, HttpResponseRedirect
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
	return HttpResponseRedirect(reverse('input_mod'))

@staff_member_required
def download(request, item_id, **kwargs):
	download = True
	item = Item_Request.objects.get(id=item_id)
	file = open(item.file.url, 'rb')
	try:
		if kwargs["read"] == 1:
			download=False
	except:
		pass
	response = FileResponse(file, as_attachment=download)
	return response

@staff_member_required
def approve(request, item_id):
	item = Item_Request.objects.get(id=item_id)
	newItem = Item(name=item.name,
		description=item.description,
		creator=item.creator)
	if item.file:
		newItem.file = item.file
	elif item.repo:
		newItem.repo = item.repo
	elif item.video:
		newItem.video = item.video
	newItem.save()
	newItem.tags.set(item.tags.all())
	item.delete()
	return HttpResponseRedirect(reverse('input_mod'))

@staff_member_required
def deny(request, item_id):
	item = Item_Request.objects.get(id=item_id).delete()
	return HttpResponseRedirect(reverse('input_mod'))