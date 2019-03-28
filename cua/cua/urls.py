"""cua URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import os

"""
 Frenzoid: We should add a suburl manipulator, in case this project gets deployed on a suburl, for example
           www.mydomain.com/cua/.
           The suburl can be changed changing the env var or using a dotenv file.
"""

suburl = '';
# If the env var is not empty, and if its value isn't "default", append the suburl.
if os.environ['SUBURL'] and os.environ['SUBURL'] != 'default':
    suburl = os.environ['SUBURL']


urlpatterns = [
    path(suburl + 'admin/', admin.site.urls),
    path(suburl, include('index.urls')),
] + static(suburl + settings.FILES_URL, document_root=settings.FILES_ROOT)
