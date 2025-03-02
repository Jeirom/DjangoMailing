from django.contrib import admin

from mailling.models import Recipient, Mail, Mailling, TryRecipient


@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'full_name', 'comment' )
    list_filter = ('email',)
    search_fields = ('email', 'id')


@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ('id', 'theme', 'body_mail' )


@admin.register(Mailling)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'startDt', 'endDt', 'my_field', 'mail', 'owner',)
    list_filter = ('my_field', )
    search_fields = ('id', )


@admin.register(TryRecipient)
class TryRecipientAdmin(admin.ModelAdmin):
    list_display = ('id', 'time_try', 'status', 'mail_response', 'recipient',)
    search_fields = ('mail_response', 'recipient', 'status',)