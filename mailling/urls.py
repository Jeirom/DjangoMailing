from django.contrib import admin
from django.urls import path, include
from django.views.generic import CreateView

from mailling.views import  MaillingDetailView, MaillingDetailView, \
    RecipientListView, \
    MaillingCreateView, MailCreateView, RecipientCreateView, CombinedTemplateView, MaillingListView, MaillingUpdateView, \
    MaillingDeleteView, TryRecipientDetailView, TryRecipientListView, TryRecipientUpdateView, TryRecipientDeleteView, \
    RecipientDetailView, MailDetailView, RecipientDeleteView, RecipientUpdateView, MailListView, MailUpdateView, \
    MailDeleteView
#HomeListView, SendMessagesHandmade,

from mailling.apps import MaillingConfig
# from maiiling.views import (RecipientListView, RecipientDetailView, RecipientCreateView, RecipientUpdateView,
#                             RecipientDeleteView, MailListView, MailDetailView, MailCreateView, MailUpdateView,
#                             MailDeleteView, HomeListView)



app_name = MaillingConfig.name

# app_name = 'mailling'




urlpatterns = [
    path('home/', MaillingListView.as_view(), name='home'),
    path('<int:pk>/detail/', MaillingDetailView.as_view(), name='mailing_detail'),
    path('create/', CombinedTemplateView.as_view(), name='mailing'),
    path('create/mailing/', MaillingCreateView.as_view(), name='create'),
    path('<int:pk>/edit_mailing/', MaillingUpdateView.as_view(), name='edit_mailing'),
    path('<int:pk>/delete_mailing/', MaillingDeleteView.as_view(), name='delete_mailing'),

    path('', TryRecipientDetailView.as_view(), name=''),
    path('<int:pk>/detail/', TryRecipientListView.as_view(), name='mailing_detail'),
    path('<int:pk>/edit_tryrecipients/', TryRecipientUpdateView.as_view(), name='edit_tryrecipients'),
    path('<int:pk>/delete_tryrecipients/', TryRecipientDeleteView.as_view(), name='delete_tryrecipients'),

    path('create/recipient/', RecipientCreateView.as_view(), name='create'),
    path('', RecipientDetailView.as_view(), name=''),
    path('<int:pk>/detail/', RecipientListView.as_view(), name='mailing_detail'),
    path('<int:pk>/edit_recipient/', RecipientUpdateView.as_view(), name='edit_recipient'),
    path('<int:pk>/delete_recipient/', RecipientDeleteView.as_view(), name='delete_recipient'),

    path('create/mail/', MailCreateView.as_view(), name='create'),
    path('<int:pk>/detail/', MailDetailView.as_view(), name='mailing_detail'),
    path('', MailListView.as_view(), name=''),
    path('<int:pk>/edit_mail/', MailUpdateView.as_view(), name='edit_mail'),
    path('<int:pk>/delete_mail/', MailDeleteView.as_view(), name='delete_mail'),


]