import logging

from django.http import HttpResponse
from django.template import loader
from volttron.models import Topics, ButtonPresses
from volttron.tables import RivaTable, TopicsTable
from django_tables2 import RequestConfig

# python debug logger
logger = logging.getLogger(__name__)


def logging(request):
    # define variable dict to pass into the template

    table = TopicsTable(Topics.objects.all())
    RequestConfig(request).configure(table)

    # getting our template
    template = loader.get_template('logging.html')

    context = {'table': table}
    # rendering the template in HttpResponse
    return HttpResponse(template.render(context, request))


def riva_logging(request):
    # define variable dict to pass into the template

    table = RivaTable(ButtonPresses.objects.all(), order_by='-pressed_datetime')
    RequestConfig(request).configure(table)

    context = {'table': table}
    # getting our template
    template = loader.get_template('logging.html')

    # rendering the template in HttpResponse
    return HttpResponse(template.render(context, request))
