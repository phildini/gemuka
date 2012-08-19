from django.http import HttpResponse
from django.template import Context, loader

def home(request):
    template = loader.get_template('home/index.html')
    context = Context()
    return HttpResponse(template.render(context))

def i_am_a(request):
    template = loader.get_template('home/iama.html')
    context = Context()
    return HttpResponse(template.render(context))