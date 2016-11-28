import logging
from django.http import HttpResponse
# importing loading from django template
from django.template import loader
# our view which is a function named index
from smartcity.vagent import hook
from smartcity.models import BacMode

logger = logging.getLogger(__name__)


def index(request, bac_mode=0):

    if bac_mode != 0:
        set_bac_mode(bac_mode)
        bac_mode = get_bac_mode()
    else:
        bac_mode = get_bac_mode()

    init_session(request)

    context = {'bac_mode': int(bac_mode)}
    # getting our template
    template = loader.get_template('index.html')

    # rendering the template in HttpResponse
    return HttpResponse(template.render(context, request))


def start_thrash_test(request, bac_mode=0):
    hook.start_thrash_test()

    if bac_mode != 0:
        set_bac_mode(bac_mode)
        bac_mode = get_bac_mode()
    else:
        bac_mode = get_bac_mode()

    request.session['start_thrash'] = 'true'
    request.session['stop_thrash'] = 'false'

    start_thrash = request.session['start_thrash']
    stop_thrash = request.session['stop_thrash']

    start_random = request.session['start_random']
    stop_random = request.session['stop_random']

    start_uniform = request.session['start_uniform']
    stop_uniform = request.session['stop_uniform']

    context = {'start_thrash': start_thrash, 'stop_thrash': stop_thrash,
               'start_random': start_random, 'stop_random': stop_random,
               'start_uniform': start_uniform, 'stop_uniform': stop_uniform,
               'bac_mode': int(bac_mode)}

    # getting our template
    template = loader.get_template('index.html')

    # rendering the template in HttpResponse
    return HttpResponse(template.render(context, request))


def stop_thrash_test(request, bac_mode=0):
    hook.stop_thrash_test()

    if bac_mode != 0:
        set_bac_mode(bac_mode)
        bac_mode = get_bac_mode()
    else:
        bac_mode = get_bac_mode()

    request.session['start_thrash'] = 'false'
    request.session['stop_thrash'] = 'true'

    start_thrash = request.session['start_thrash']
    stop_thrash = request.session['stop_thrash']

    start_random = request.session['start_random']
    stop_random = request.session['stop_random']

    start_uniform = request.session['start_uniform']
    stop_uniform = request.session['stop_uniform']

    context = {'start_thrash': start_thrash, 'stop_thrash': stop_thrash,
               'start_random': start_random, 'stop_random': stop_random,
               'start_uniform': start_uniform, 'stop_uniform': stop_uniform,
               'bac_mode': int(bac_mode)}

    # getting our template
    template = loader.get_template('index.html')

    # rendering the template in HttpResponse
    return HttpResponse(template.render(context, request))


def start_random_test(request, bac_mode=0):
    hook.start_random_test()

    if bac_mode != 0:
        set_bac_mode(bac_mode)
        bac_mode = get_bac_mode()
    else:
        bac_mode = get_bac_mode()

    request.session['start_random'] = 'true'
    request.session['stop_random'] = 'false'

    start_thrash = request.session['start_thrash']
    stop_thrash = request.session['stop_thrash']

    start_random = request.session['start_random']
    stop_random = request.session['stop_random']

    start_uniform = request.session['start_uniform']
    stop_uniform = request.session['stop_uniform']

    context = {'start_thrash': start_thrash, 'stop_thrash': stop_thrash,
               'start_random': start_random, 'stop_random': stop_random,
               'start_uniform': start_uniform, 'stop_uniform': stop_uniform,
               'bac_mode': int(bac_mode)}

    # getting our template
    template = loader.get_template('index.html')

    # rendering the template in HttpResponse
    return HttpResponse(template.render(context, request))


def stop_random_test(request, bac_mode=0):
    hook.stop_random_test()

    if bac_mode != 0:
        set_bac_mode(bac_mode)
        bac_mode = get_bac_mode()
    else:
        bac_mode = get_bac_mode()

    request.session['start_random'] = 'false'
    request.session['stop_random'] = 'true'

    start_thrash = request.session['start_thrash']
    stop_thrash = request.session['stop_thrash']

    start_random = request.session['start_random']
    stop_random = request.session['stop_random']

    start_uniform = request.session['start_uniform']
    stop_uniform = request.session['stop_uniform']

    context = {'start_thrash': start_thrash, 'stop_thrash': stop_thrash,
               'start_random': start_random, 'stop_random': stop_random,
               'start_uniform': start_uniform, 'stop_uniform': stop_uniform,
               'bac_mode': int(bac_mode)}

    # getting our template
    template = loader.get_template('index.html')

    # rendering the template in HttpResponse
    return HttpResponse(template.render(context, request))


def start_uniform_test(request, bac_mode=0):
    hook.start_uniform_test()

    if bac_mode != 0:
        set_bac_mode(bac_mode)
        bac_mode = get_bac_mode()
    else:
        bac_mode = get_bac_mode()

    request.session['start_uniform'] = 'true'
    request.session['stop_uniform'] = 'false'

    start_thrash = request.session['start_thrash']
    stop_thrash = request.session['stop_thrash']

    start_random = request.session['start_random']
    stop_random = request.session['stop_random']

    start_uniform = request.session['start_uniform']
    stop_uniform = request.session['stop_uniform']

    context = {'start_thrash': start_thrash, 'stop_thrash': stop_thrash,
               'start_random': start_random, 'stop_random': stop_random,
               'start_uniform': start_uniform, 'stop_uniform': stop_uniform,
               'bac_mode': int(bac_mode)}

    # getting our template
    template = loader.get_template('index.html')

    # rendering the template in HttpResponse
    return HttpResponse(template.render(context, request))


def stop_uniform_test(request, bac_mode=0):
    hook.stop_uniform_test()

    if bac_mode != 0:
        set_bac_mode(bac_mode)
        bac_mode = get_bac_mode()
    else:
        bac_mode = get_bac_mode()

    request.session['start_uniform'] = 'false'
    request.session['stop_uniform'] = 'true'

    start_thrash = request.session['start_thrash']
    stop_thrash = request.session['stop_thrash']

    start_random = request.session['start_random']
    stop_random = request.session['stop_random']

    start_uniform = request.session['start_uniform']
    stop_uniform = request.session['stop_uniform']

    context = {'start_thrash': start_thrash, 'stop_thrash': stop_thrash,
               'start_random': start_random, 'stop_random': stop_random,
               'start_uniform': start_uniform, 'stop_uniform': stop_uniform,
               'bac_mode': int(bac_mode)}

    # getting our template
    template = loader.get_template('index.html')

    # rendering the template in HttpResponse
    return HttpResponse(template.render(context, request))


def init_session(request):
    request.session['start_thrash'] = ''
    request.session['stop_thrash'] = ''
    request.session['start_random'] = ''
    request.session['stop_random'] = ''
    request.session['start_uniform'] = ''
    request.session['stop_uniform'] = ''


def set_bac_mode(bac_mode):
    query = BacMode(current_mode=bac_mode)
    query.save()


def get_bac_mode():
    query = BacMode.objects.values('current_mode').order_by("-mode_id")[0]
    return int(query['current_mode'])
