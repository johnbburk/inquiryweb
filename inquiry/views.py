from django.template import Context, loader
from django.http import HttpResponse
from inquiry.models import Event

def index(request):
    latest_question_list = Event.objects.all().order_by('mod_datetime')
    t = loader.get_template('index.html')
    c = Context({
        'latest_question_list':latest_question_list,
    })
    return HttpResponse(t.render(c))