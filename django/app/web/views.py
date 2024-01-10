from django.http import HttpResponse
def sayhello(request):
    return HttpResponse("<h1>salam be shoma az view e django azizane man</h1>")