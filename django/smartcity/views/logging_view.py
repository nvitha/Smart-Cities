#import logging
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from smartcity.models import Data
from smartcity.tables import DjangoRivaTable, BacTable, RivaCommandsTable
from django_tables2 import RequestConfig


def logging(request):

    # define variable dict to pass into the template
    table_type = 'riva'

    sim_table = DjangoRivaTable(Data.objects.filter(topic_id=15), order_by='-ts')
    RequestConfig(request).configure(sim_table)

    command_table = RivaCommandsTable(Data.objects.filter(Q(topic_id=11) |
                                                          Q(topic_id=12) |
                                                          Q(topic_id=13) |
                                                          Q(topic_id=14)
                                                          ), order_by='-ts')

    RequestConfig(request).configure(command_table)

    context = {'sim_table': sim_table, 'command_table': command_table, 'table_type': 'riva'}
    # getting our template
    template = loader.get_template('logging.html')

    # rendering the template in HttpResponse
    return HttpResponse(template.render(context, request))


def bac_logging(request):
    table_type = 'bac'

    table = BacTable(Data.objects.filter(topic_id=10), order_by='-ts')
    RequestConfig(request).configure(table)
    query = Data.objects.all()
    context = {'bac_table': table, 'table_type': 'bac'}
    # getting our template
    template = loader.get_template('logging.html')

    # rendering the template in HttpResponse
    return HttpResponse(template.render(context, request))
