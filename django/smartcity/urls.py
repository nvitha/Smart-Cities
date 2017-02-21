"""SmartCity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.contrib.auth import views as auth_views

from smartcity.views import index_view
from smartcity.views import metrics_view
from smartcity.views import logging_view

urlpatterns = [
    # Admin UI
    url(r'^admin/', admin.site.urls),

    # Login/Logout Page
    url(r'^$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),

    # Home Page
    url(r'^home$', index_view.index, name='index'),
    # Home Page Test Button Ajax Call
    url(r'^bac_test/$', index_view.start_test),
    # Home Page BAC Switch Ajax Call
    url(r'^bac_mode/$', index_view.change_bac_mode),


    # Metrics View
    url(r'^metrics/', metrics_view.metrics, name='metrics'),
    # Logging View
    url(r'^logging/$', logging_view.logging, name='logging'),
    url(r'^logging/bac/$', logging_view.bac_logging, name='bac_logging'),
    url(r'^logging/volttron/$', logging_view.logging, name='volttron_logging'),


]
