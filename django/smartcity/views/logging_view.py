#import logging
from django.http import HttpResponse
from django.template import loader
from smartcity.models import ButtonPresses
from smartcity.tables import RivaTable
from django_tables2 import RequestConfig


def logging(request):

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
