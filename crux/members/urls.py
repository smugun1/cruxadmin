"""crux URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from . import views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('signup/', views.sign_up, name='signup'),
                  path('user_login/', auth_views.LoginView.as_view(template_name='authenticate/userlogin.html'),
                       name='login'),
                  path('user_logout/', auth_views.LoginView.as_view(template_name='authenticate/userlogout.html'),
                       name='logout'),
                  path('', include('qrux.urls')),

                  path('members/', include('django.contrib.auth.urls')),
                  path('members/', include('members.urls')),
              ] 
