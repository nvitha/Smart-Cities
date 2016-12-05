import logging
from django.http import HttpResponse
# importing loading from django template
from django.template import loader
# our view which is a function named index
from smartcity.vagent import hook
from smartcity.models import Data
from smartcity.models import RivaConnection

logger = logging.getLogger(__name__)


def index(request, bac_mode=0, test_mode='', refresh_flag=''):

    riva_status = get_riva_status()

    if bac_mode != 0:
        set_bac_mode(bac_mode, request)
        bac_mode = get_bac_mode(request)
    else:
        bac_mode = init_bac_mode(request)

    if test_mode != '':
        select_test(test_mode)
        session_test(test_mode, request)
    else:
        init_session(request)

    last_test = get_last_test()

    start_thrash = request.session['start_thrash']
    stop_thrash = request.session['stop_thrash']

    start_random = request.session['start_random']
    stop_random = request.session['stop_random']

    start_uniform = request.session['start_uniform']
    stop_uniform = request.session['stop_uniform']

    context = {'start_thrash': start_thrash, 'stop_thrash': stop_thrash,
               'start_random': start_random, 'stop_random': stop_random,
               'start_uniform': start_uniform, 'stop_uniform': stop_uniform,
               'bac_mode': int(bac_mode), 'riva_status': riva_status,
               'last_test': last_test}

    # getting our template
    template = loader.get_template('index.html')

    # rendering the template in HttpResponse
    return HttpResponse(template.render(context, request))


def get_riva_status():
    query = RivaConnection.objects.values('conn_status').order_by("-conn_id")[0]

    if int(query['conn_status']) == 1:
        return 'Connected'
    else:
        return 'Disconnected'


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


def session_test(test_mode, request):

    if test_mode == 'start_thrash':
        request.session['start_thrash'] = 'true'
        request.session['stop_thrash'] = 'false'
    elif test_mode == 'stop_thrash':
        request.session['start_thrash'] = 'false'
        request.session['stop_thrash'] = 'true'
    elif test_mode == 'start_random':
        request.session['start_random'] = 'true'
        request.session['stop_random'] = 'false'
    elif test_mode == 'stop_random':
        request.session['start_random'] = 'false'
        request.session['stop_random'] = 'true'
    elif test_mode == 'start_uniform':
        request.session['start_uniform'] = 'true'
        request.session['stop_uniform'] = 'false'
    elif test_mode == 'stop_uniform':
        request.session['start_uniform'] = 'false'
        request.session['stop_uniform'] = 'true'


def init_session(request):
    if 'start_thrash' not in request.session:
        request.session['start_thrash'] = ''
    if 'stop_thrash' not in request.session:
        request.session['stop_thrash'] = ''
    if 'start_random' not in request.session:
        request.session['start_random'] = ''
    if 'stop_random' not in request.session:
        request.session['stop_random'] = ''
    if 'start_uniform' not in request.session:
        request.session['start_uniform'] = ''
    if 'stop_uniform' not in request.session:
        request.session['stop_uniform'] = ''


def set_bac_mode(bac_mode, request):
    if bac_mode == '1':
        hook.bac_mode_one()
        request.session['bac_mode'] = 1
    elif bac_mode == '2':
        hook.bac_mode_two()
        request.session['bac_mode'] = 2
    elif bac_mode == '3':
        hook.bac_mode_three()
        request.session['bac_mode'] = 3
    elif bac_mode == '4':
        hook.bac_mode_four()
        request.session['bac_mode'] = 4


def get_bac_mode(request):
    return request.session['bac_mode']


def init_bac_mode(request):
    query = Data.objects.filter(topic_id=1).values('value_string').order_by("-ts")[0]
    bac_mode = int(query['value_string'][-2])
    request.session['bac_mode'] = bac_mode
    return bac_mode


def get_last_test():
    query = Data.objects.filter(topic_id=4).values('value_string').order_by("-ts")[0]

    value = query['value_string']

    if value == '"st"':
        return 'Start Thrashing Test'
    elif value == '"et"':
        return 'End Thrashing Test'
    elif value == '"su"':
        return 'Start Flood Test'
    elif value == '"eu"':
        return 'End Flood Test'
    elif value == '"sr"':
        return 'Start Random Flood Test'
    elif value == '"er"':
        return 'End Random Flood Test'
