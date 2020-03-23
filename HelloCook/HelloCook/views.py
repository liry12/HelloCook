from django.http import HttpResponse

def index(request):
    return HttpResponse("This is a start of HelloCook!")

