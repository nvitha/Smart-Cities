"""volttron URL Configuration

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

from volttron.views import index_view
from volttron.views import metrics_view
from volttron.views import logging_view

urlpatterns = [
    # Admin UI
    url(r'^admin/', admin.site.urls),
    # Home Page
    url(r'^$', index_view.index, name='index'),
    # Metrics View
    url(r'^metrics/', metrics_view.metrics, name='metrics'),
    # Logging View
    url(r'^logging/$', logging_view.logging, name='logging'),
    url(r'^logging/riva/$', logging_view.riva_logging, name='riva_logging'),
    url(r'^logging/bac/$', logging_view.riva_logging, name='bac_logging'),
    url(r'^logging/volttron/$', logging_view.riva_logging, name='volttron_logging'),

]
