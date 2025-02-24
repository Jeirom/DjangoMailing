from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView, FormView, View)
from pyexpat.errors import messages

from mailling.forms import GoMail, RecipientForm, MailForm, MaillingForm
from mailling.models import Recipient, Mail, Mailling, TryRecipient
from django.core.mail import send_mail


class MailingDetailView(DetailView):
    model = Mailling
    template_name = 'mailing_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipients'] = Recipient.objects.all()
        context['mails'] = Mail.objects.all()
        context['mailings'] = Mailling.objects.select_related('mail', 'recipient').all()
        context['tryrecipients'] = TryRecipient.objects.all()
        return context


class RecipientListView(ListView):
    template_name = 'create.html'
    model = Mail


class SendMessagesHandmade(FormView):
    model = Mail
    template_name = 'send_messages_handmade.html'
    form_class = GoMail
    success_url = reverse_lazy('mailling:home')

    def form_valid(self, form):
        # Сохраняем сообщение
        message = form.save()
        # Здесь можно добавить логику для отправки сообщения
        # send_email(message.subject, message.body)
        return super().form_valid(form)

    def form_invalid(self, form):
        # Здесь можно добавить обработку невалидной формы, если необходимо
        return super().form_invalid(form)


class HomeListView(ListView):
    model = Mailling
    context_object_name = "maillings"
    template_name = "home.html"



# class RecipientListView(ListView):
#     model = Recipient
#
#
# class RecipientDetailView(DetailView):
#     model = Recipient
#
#
class RecipientCreateView(CreateView):
    model = Recipient
    template_name = 'create_recipient.html'
    form_class = RecipientForm
    success_url = reverse_lazy('mailling:create')
#
#
# class RecipientDeleteView(DeleteView):
#     model = Recipient
#
#
# class RecipientUpdateView(UpdateView):
#     model = Recipient
#
#
# class MailListView(ListView):
#     model = Mail
#
#
# class MailDetailView(DetailView):
#     model = Mail
#
#
class MailCreateView(CreateView):
    model = Mail
    template_name = 'create_mail.html'
    form_class = MailForm
    success_url = reverse_lazy('mailling:create')
#
#
# class MailUpdateView(UpdateView):
#     model = Mail
#
#
# class MailDeleteView(DeleteView):
#     model = Mail
#
#
class MaillingCreateView(CreateView):
    model = Mailling
    template_name = 'create_mailling.html'
    form_class = MaillingForm
    success_url = reverse_lazy('mailling:create')
#
#
class MaillingDetailView(DetailView):
    model = Mailling
    template_name = 'mailling_detail.html'

#
# class MaillingListView(ListView):
#     model = Mailling
#
#
# class MaillingListView(ListView):
#     model = Mailling
#
#
# class MaillingListView(ListView):
#     model = Mailling
#
