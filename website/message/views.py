from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {
        'title': 'Send Message'
    })


def send(request):
    return render(request, 'send.html', {
        'title': 'Send Message'
    })


def read(request):
    return render(request, 'read.html', {
        'title': 'Send Message'
    })