from django.core.management.base import BaseCommand
from mailling.models import Mail
from mailling.views import SendMessagesHandmade


# from mailling.views import   # Импортируйте функцию отправки

class Command(BaseCommand):
    help = 'Отправляет все неподтвержденные сообщения'

    def handle(self, *args, **kwargs):
        messages = Mail.objects.filter(is_sent=False)
        for message in messages:
            SendMessagesHandmade(message.subject, message.body)
            message.is_sent = True
            message.save()
            self.stdout.write(self.style.SUCCESS(f'Сообщение "{message.subject}" отправлено.'))