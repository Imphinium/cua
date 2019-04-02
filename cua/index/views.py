from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from mod.models import *
from django.http import JsonResponse, FileResponse, HttpResponseRedirect
from .forms import ItemUploadForm
from django.db.models import Q
from django.contrib.auth.views import login_required
import requests
import os

# Utilidades

def validate_repo(repo):
	u = requests.get("https://github.com/{0}".format(repo))
	if u.status_code == 404:
		return False
	return True

def validate_video(video):
	u = requests.get("http://www.youtube.com/oembed?url=http://www.youtube.com/watch?v={0}&format=json".format(video))
	if u.status_code == 404:
		return False
	return True

def validate_tags(tags):
	tags = tags.split(" ")
	tagsObj = []
	for tag in tags:
		tagObj = Tag.objects.filter(name=tag)
		if tagObj.exists():
			tagsObj.append(tagObj.get())
		else:
			tagObj = Tag(name=tag)
			tagObj.save()
			tagsObj.append(tagObj)
	return tagsObj


# Create your views here.

def index(request):
	return render(request, 'index/index.html')

def results(request):
	if request.method == 'GET':
		results = Item.objects.all()
		query = request.GET.get("query")
		if query:
			results = results.filter(Q(name__icontains=query) | Q(description__icontains=query))
		tags = request.GET.getlist("tags")
		if tags:
			results = results.filter(tags__in=tags)
		context = {"results": results}
		return render(request, 'index/results.html', context)
	else:
		return render(request, 'index/index.html')

def details(request, item_id):
	if item_id:
		item = Item.objects.filter(id=item_id)
		if item.exists():
			context = {"item": item.get()}
			return render(request, 'index/details.html', context)
	return HttpResponseRedirect(reverse('index'))

def upload(request):
	if request.method == 'POST':
		form = ItemUploadForm(request.POST, request.FILES)
		if form.is_valid():
			data = form.cleaned_data
			print(data)
			tags = validate_tags(data["tags"])
			itemReqObj = Item_Request(name=data["name"],
				description=data["description"])
			if data["file"]:
				itemReqObj.file = data["file"]
			elif data["video"] != '':
				if validate_video(data["video"]):
					itemReqObj.video = data["video"]
				else:
					return JsonResponse({'error': True, 'errors': 'Incorrect video'})
			elif data["repo"] != '':
				if validate_repo(data["repo"]):
					itemReqObj.repo = data["repo"]
				else:
					return JsonResponse({'error': True, 'errors': 'Incorrect repo'})
			itemReqObj.save()
			itemReqObj.tags.set(tags)

			return JsonResponse({'error': False, 'message': 'Uploaded Successfully'})
		else:
			return JsonResponse({'error': True, 'errors': form.errors})
	else:
		form = ItemUploadForm()
		return render(request, 'index/upload.html', {'form': form})

def download(request, item_id):
	item = Item.objects.get(id=item_id)
	file = open(item.file.url, 'rb')
	response = FileResponse(file, as_attachment=True)
	return response