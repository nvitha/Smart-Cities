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
    url(r'^test=(?P<test_mode>[A-Za-z]+_[A-Za-z]+)/$', index_view.index, name='test'),

    # Manually Refresh Status
    url(r'^refresh=(?P<refresh_flag>[A-Za-z]+)$', index_view.index, name='refresh_status'),

    # Index BAC
    url(r'^mode_(?P<bac_mode>[1-4]+)/$', index_view.index, name='select_mode'),

    # Metrics View
    url(r'^metrics/', metrics_view.metrics, name='metrics'),
    # Logging View
    url(r'^logging/$', logging_view.logging, name='logging'),
    url(r'^logging/bac/$', logging_view.bac_logging, name='bac_logging'),
    url(r'^logging/volttron/$', logging_view.logging, name='volttron_logging'),


]
