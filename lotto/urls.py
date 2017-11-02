"""lotto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views
#from .views import FacebookLogin
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

from ticket.views import createTicket

urlpatterns = [

    #admin
    url(r'^admin/', admin.site.urls),

    # root link
    url(r'^$', views.api_root),

    #auth and registration links
    url(r'^rest-auth/', include('rest_auth.urls', namespace="rest-auth")),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    #url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),

   # url(r'^signup/$', TemplateView.as_view(template_name="rest_auth/signup.html"), name='signup'),
    #url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^auth/', include('rest_framework_social_oauth2.urls')),
    #rest_framework
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest-framework')),

    #users links
    url(r'^', include('userprofile.urls', namespace='users')),  
    #lottery links
    url(r'^', include('lottery.urls', namespace='lottery')),  
  
    url(r'^ticket-generator/', createTicket, name='create-ticket'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
