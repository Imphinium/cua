from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import logout
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

@staff_member_required
def index(request):
	return render(request, 'mod/index.html')

@staff_member_required
def logout_view(request):
	if request.user.is_authenticated:
		logout(request)
	return HttpResponseRedirect(reverse('index'))