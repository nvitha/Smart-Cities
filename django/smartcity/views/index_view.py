import logging
from django.http import HttpResponse
# importing loading from django template
from django.template import loader
# our view which is a function named index
from smartcity.vagent import hook


logger = logging.getLogger(__name__)


def index(request):
    context = {}
    # getting our template
    template = loader.get_template('index.html')

    # rendering the template in HttpResponse
    return HttpResponse(template.render(context, request))


def publish(request):

    hook.publish_test()

    context = {'published': 'Test request sent to message bus.'}

    # getting our template
    template = loader.get_template('index.html')

    # rendering the template in HttpResponse
    return HttpResponse(template.render(context, request))


def click_to_publish():
    hook.publish_test()