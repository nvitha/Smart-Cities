#import logging
from itertools import groupby
from datetime import datetime
from django.http import HttpResponse
from django.template import loader
from django.db.models import Count
from smartcity.models import ButtonPresses

# python debug logger
#logger = logging.getLogger(__name__)


def metrics(request):

    summed_data = get_button_over_time()
    parsed_data = parse_summed_data(summed_data)
    button_counts = get_value_counts()
    date_data = [i for i in xrange(1,31)]
    context = {'button_counts': button_counts, 'summed_data': parsed_data, 'date_data': date_data}

    # getting our template
    template = loader.get_template('metrics.html')
    # rendering the template in HttpResponse
    return HttpResponse(template.render(context, request))

def parse_summed_data(summed_data):

    i = 0
    ordered_data = []

    lookup = {}
    for item in summed_data:
        lookup[int(item[0])] = item[1]

    for i in xrange(1, 31):
        if i in lookup:
            ordered_data.append(lookup[i])
        else:
            ordered_data.append(0)

    return ordered_data

def get_value_counts():
    data = ButtonPresses.objects.values('button_pressed').annotate(the_count=Count('button_pressed'))
    values = []
    for item in data:
        if item['the_count'] > 10:
            values.append(item['the_count'])
    return values


def get_button_over_time():

    data = ButtonPresses.objects.values_list('button_pressed', 'pressed_datetime')
    binned_data = [[] for _ in range(4)]
    for row in data:
        if int(row[0]) < 4:
            binned_data[int(row[0])].append((int(row[0]), int(row[1].strftime("%d"))))

    i = 0
    summed_data = [[] for _ in range(4)]
    for this_bin in binned_data:
        bin_dict = {}
        this_bin.sort()
        for item in this_bin:
            if item[1] not in bin_dict:
                bin_dict[item[1]] = 1
            else:
                bin_dict[item[1]] += 1
        bin_tups = bin_dict.items()
        bin_list = [list(item) for item in bin_tups]
        summed_data[i].append(bin_list)
        i += 1

    value_bins = [[] for _ in range(4)]
    date_bins = [[] for _ in range(4)]

    i = 0
    for this_bin in summed_data:
        value_list = []
        date_list = []
        for item in this_bin:
            date_list.append(item[0])
            value_list.append(item[1])
        value_bins[i].append(value_list)
        date_bins[i].append(date_list)
        i += 1

    return summed_data[0][0]

