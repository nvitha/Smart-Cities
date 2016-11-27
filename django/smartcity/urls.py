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

from smartcity.views import index_view
from smartcity.views import metrics_view
from smartcity.views import logging_view

urlpatterns = [
    # Admin UI
    url(r'^admin/', admin.site.urls),
    # Home Page
    url(r'^$', index_view.index, name='index'),

    # Index Smart Meter
    url(r'^refresh_status$', index_view.index, name='refresh_status'),
    url(r'^start_thrash/$', index_view.start_thrash_test, name='start_thrash'),
    url(r'^stop_thrash/$', index_view.stop_thrash_test, name='stop_thrash'),
    url(r'^start_random/$', index_view.start_random_test, name='start_random'),
    url(r'^stop_random/$', index_view.stop_random_test, name='stop_random'),
    url(r'^start_uniform/$', index_view.start_uniform_test, name='start_uniform'),
    url(r'^stop_uniform/$', index_view.stop_uniform_test, name='stop_uniform'),

    # Index BAC
    url(r'^mode_one/$', index_view.mode_one, name='mode_one'),
    url(r'^mode_two/$', index_view.mode_one, name='mode_two'),
    url(r'^mode_three/$', index_view.mode_one, name='mode_three'),
    url(r'^mode_four/$', index_view.mode_one, name='mode_four'),
    
    # Metrics View
    url(r'^metrics/', metrics_view.metrics, name='metrics'),
    # Logging View
    url(r'^logging/$', logging_view.logging, name='logging'),
    url(r'^logging/riva/$', logging_view.riva_logging, name='riva_logging'),
    url(r'^logging/bac/$', logging_view.riva_logging, name='bac_logging'),
    url(r'^logging/volttron/$', logging_view.riva_logging, name='volttron_logging'),


]
