from django.contrib import admin
from .models import Message, Reply, Reader

# Register your models here.
admin.site.register(Message)
admin.site.register(Reply)
admin.site.register(Reader)
