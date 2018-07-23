from django.db import models

# Create your models here.


class Message(models.Model):
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sender = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name="Sender")
    recipient = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name="Receiver")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

class Reply(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name="Author")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['created_at']
