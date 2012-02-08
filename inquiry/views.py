from django.http import HttpResponse
def index(request):
    return HttpResponse("This is the default page for inquiryweb")