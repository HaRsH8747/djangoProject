from django.contrib import admin

from Messaging.models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'timestamp')
    search_fields = ('sender__username', 'receiver__username', 'content')


admin.site.register(Message, MessageAdmin)
