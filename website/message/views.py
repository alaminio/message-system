from django.shortcuts import render, redirect
from .models import Message, Reply, Reader
from .forms import MessageForm, ReplyForm
from pprint import pprint
from django.contrib.auth.models import User
from datetime import datetime


# Create your views here.
def index(request):

    if request.user.is_authenticated:
        messages = Message.objects.filter(recipient=request.user.id)
        ccMessages = Reader.objects.filter(cc=request.user.id)
        logged_in = True
    else:
        messages = []
        ccMessages = []
        logged_in = False

    return render(request, 'index.html', {
        'title': 'Message System inbox',
        'messages': messages,
        'ccMessages': ccMessages,
        'logged_in': logged_in
    })


def send(request):
    if request.user.is_authenticated:
        logged_in = True
    else:
        logged_in = False

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            # message = form.save(commit=False)
            # message.sender = request.user
            # message.save()
            message = Message()
            message.subject = form.cleaned_data['subject']
            message.message = form.cleaned_data['message']
            message.sender = request.user
            recipient = form.cleaned_data['recipient']
            message.recipient = recipient
            message.created_at = datetime.now()
            message.save()

            ccUsers = form.cleaned_data['cc']
            for cc in ccUsers:
                if recipient == cc:
                    continue
                reader = Reader()
                reader.cc = cc
                reader.message = message
                reader.save()

            return redirect('/read/{}'.format(message.pk))
    else:
        form = MessageForm()
    return render(request, 'send.html', {
        'title': 'Send Message',
        'form': form,
        'logged_in': logged_in
    })


def read(request, id):
    if request.user.is_authenticated:
        logged_in = True
    else:
        logged_in = False

    title = "Read message"

    message = Message.objects.get(pk=id)
    if message and message.subject:
        title = message.subject

    replies = Reply.objects.filter(message=message)
    can_replay = False

    if message.recipient == request.user or message.sender == request.user:
        can_replay = True

    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.message = message
            reply.author = request.user
            reply.save()
    else:
        form = ReplyForm()


    return render(request, 'read.html', {
        'title': title,
        'message': message,
        'form': form,
        'replies': replies,
        'can_replay': can_replay,
        'logged_in': logged_in
    })
