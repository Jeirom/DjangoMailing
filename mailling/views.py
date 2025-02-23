from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView, FormView)

from mailling.forms import GoMail
from mailling.models import Recipient, Mail, Mailling
from django.core.mail import send_mail


class SendMessagesHandmade(FormView):
    model = Mail
    template_name = 'send_messages_handmade.html'
    form_class = GoMail
    success_url = reverse_lazy('home.html')

    # def form_valid(self, form):
    #     # Сохраняем сообщение
    #     message = form.save()
    #     # Здесь можно добавить логику для отправки сообщения
    #     # send_email(message.subject, message.body)
    #     return super().form_valid(form)
    #
    # def form_invalid(self, form):
    #     # Здесь можно добавить обработку невалидной формы, если необходимо
    #     return super().form_invalid(form)


class HomeListView(ListView):
    model = Mailling
    template_name = "home.html"



# class RecipientListView(ListView):
#     model = Recipient
#
#
# class RecipientDetailView(DetailView):
#     model = Recipient
#
#
# class RecipientCreateView(CreateView):
#     model = Recipient
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
# class MailCreateView(CreateView):
#     model = Mail
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
# class MaillingListView(ListView):
#     model = Mailling
#
#
# class MaillingDetailView(DetailView):
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
#
# class MaillingListView(ListView):
#     model = Mailling
#
