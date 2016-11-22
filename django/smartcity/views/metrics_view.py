#import logging
from django.http import HttpResponse
from django.template import loader
from django.db.models import Count
from smartcity.models import ButtonPresses

# python debug logger
#logger = logging.getLogger(__name__)


def metrics(request):

    button_counts = get_value_counts()
    context = {'button_counts': button_counts}
    #print context[button_counts]
    # getting our template
    template = loader.get_template('metrics.html')
    # rendering the template in HttpResponse
    return HttpResponse(template.render(context, request))


def get_value_counts():
    data = ButtonPresses.objects.values('button_pressed').annotate(the_count=Count('button_pressed'))
    values = []
    for item in data:
        if item['the_count'] > 10:
            values.append(item['the_count'])
    return values

