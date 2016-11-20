import logging

from django.http import HttpResponse
from django.template import loader
from volttron.models import ButtonPresses
from volttron.tables import RivaTable
from django_tables2 import RequestConfig
from volttron.vagent.django_agent import agent

# python debug logger
logger = logging.getLogger(__name__)


def logging(request):

    agent.publish_message()
    # define variable dict to pass into the template

    table = RivaTable(ButtonPresses.objects.all(), order_by='-pressed_datetime')
    RequestConfig(request).configure(table)

    context = {'table': table}
    # getting our template
    template = loader.get_template('logging.html')

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
