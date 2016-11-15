from django.http import HttpResponse

# importing loading from django template
from django.template import loader
# our view which is a function named index


def index(request):

    # define variable dict to pass into the template
    context = {'name': 'malcolm', 'lname': 'chaney'}

    # getting our template
    template = loader.get_template('index.html')

    # rendering the template in HttpResponse
    return HttpResponse(template.render(context, request))
