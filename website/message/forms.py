from django import forms
from .models import Message, Reply
from django.contrib.auth.models import User


class MessageForm(forms.Form):
    subject = forms.CharField(max_length=255)
    recipient = forms.ModelChoiceField(queryset=User.objects.all())
    message = forms.CharField(widget=forms.Textarea)
    cc = forms.ModelMultipleChoiceField(queryset=User.objects.all())

    class Meta():
        model = Message
        #fields = ('subject', 'recipient', 'message',)


class ReplyForm(forms.ModelForm):

    class Meta():
        model = Reply
        fields = ('text',)
