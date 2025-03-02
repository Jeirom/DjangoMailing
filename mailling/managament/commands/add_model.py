from mailling.models import Recipient, Mail, Mailling, TryRecipient
recipient = Recipient.objects.create(email='test@gmail.com', full_name='Test')
mail = Mail.objects.create(theme='Тема тест', body_mail='Письмо тест')
recipient.save()
mail.save()
mailing = Mailling.objects.create(startDt='2025-02-24 11:51:00+00', endDt='2025-02-24 11:51:00+00', mail=mail)
mailing.save()
tryrecipient = TryRecipient.objects.create(time_try='2025-02-24 12:11:00+00', mail_response='200', recipient=recipient)
tryrecipient.save()
