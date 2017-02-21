import logging

from django.http import HttpResponse
from django.template import loader

# our view which is a function named index
from smartcity.vagent import hook
from smartcity.models import Data
from smartcity.models import RivaConnection

logger = logging.getLogger(__name__)


# print debug statements go to /var/log/apache2/error.log
def index(request):

    # query database for current riva connection status
    riva_status = get_riva_status()

    # query database for current bac mode
    bac_mode = get_bac_mode()
    bac_mode_text = get_bac_mode_text(bac_mode)

    # query database for last test conducted
    last_test = get_last_test()

    context = {'bac_mode': int(bac_mode), 'bac_mode_text': bac_mode_text, 'riva_status': riva_status, 'last_test': last_test}

    # getting our template
    template = loader.get_template('index.html')

    # rendering the template in HttpResponse
    return HttpResponse(template.render(context, request))


def change_bac_mode(request):
    if request.method == 'POST':
        mode = request.POST['mode']
        set_bac_mode(mode)

    return HttpResponse(request)


def start_test(request):
    # print 'Called Function: start_test'
    if request.method == 'POST':
        test = request.POST['test']
        select_test(test)

    return HttpResponse(request)


def get_riva_status():
    query = RivaConnection.objects.values('conn_status').order_by("-conn_id")[0]

    if int(query['conn_status']) == 1:
        return 'Connected'
    else:
        return 'Disconnected'


def get_bac_mode():
    query = Data.objects.filter(topic_id=10).values('value_string').order_by("-ts")[0]
    bac_mode = int(query['value_string'][-2])
    return bac_mode


def get_bac_mode_text(bac_mode):
    if bac_mode == 1:
        return 'Day Mode'
    elif bac_mode == 2:
        return 'Night Mode'
    elif bac_mode == 3:
        return 'Vacant Mode'
    elif bac_mode == 4:
        return 'Emergency Mode'
    elif bac_mode == 0:
        return 'Shutdown'


def set_bac_mode(bac_mode):
    if bac_mode == '1':
        hook.bac_mode_one()
    elif bac_mode == '2':
        hook.bac_mode_two()
    elif bac_mode == '3':
        hook.bac_mode_three()
    elif bac_mode == '4':
        hook.bac_mode_four()
    elif bac_mode == '0':
        hook.bac_mode_zero()


def select_test(test_mode):
    if test_mode == 'start_thrash':
        hook.start_thrash_test()
    elif test_mode == 'stop_thrash':
        hook.stop_thrash_test()
    elif test_mode == 'start_random':
        hook.start_random_test()
    elif test_mode == 'stop_random':
        hook.stop_random_test()
    elif test_mode == 'start_uniform':
        hook.start_uniform_test()
    elif test_mode == 'stop_uniform':
        hook.stop_uniform_test()


def get_last_test():
    query = Data.objects.filter(topic_id=15).values('value_string').order_by("-ts")[0]

    value = query['value_string']

    if value == '"st"':
        return 'Thrashing Test'
    elif value == '"et"':
        return 'Thrashing Test'
    elif value == '"su"':
        return 'Flood Test'
    elif value == '"eu"':
        return 'Flood Test'
    elif value == '"sr"':
        return 'Random Flood Test'
    elif value == '"er"':
        return 'Random Flood Test'
