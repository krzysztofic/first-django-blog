from django.contrib import admin
from .models import Message

class AdminMessage(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject']
    list_display_links = ('subject',)


admin.site.register(Message, AdminMessage)
