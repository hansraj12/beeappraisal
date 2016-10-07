"""beeappraisal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import patterns
from appraisal.views import *
 
urlpatterns = patterns('',
    url(r'^admin/', admin.site.urls),
    url(r'^login/', admin_login),
    url(r'^home/', home, name='home'),  
    url(r'^success/', success, name='success'),
    url(r'^appraiserlogin/', appraiserlogin, name='appraiserlogin') ,
    url(r'^appraiserhome/(?P<username>\w+)', appraiserhome, name='appraiserhome') ,
    url(r'^appraiser/(?P<uname>\w+)', appraiser, name='appraiser') ,
    url(r'^app_role/(?P<uname>\w+)', app_role, name='app_role'),
    url(r'^app_role_select/(?P<uname>\w+)', app_role_select, name='app_role_select'),
    url(r'^success_appraiser/(?P<uname>\w+)', success_appraiser, name='success_appraiser'),
    url(r'^success_app_role/(?P<uname>\w+)', success_app_role, name='success_app_role'),
    url(r'^help/(?P<uname>\w+)', help, name='help'),
    url(r'^logout_admin', logout_view_admin),
    url(r'^logout', logout_view_appraiser),
)