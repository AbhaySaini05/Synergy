from django.contrib import admin
from comm.models import Server, Channel, Message

# Register your models here.
admin.site.register(Server)
admin.site.register(Channel)
admin.site.register(Message)
