from django.contrib import admin
from django.urls import path, include

from mailling.views import HomeListView, SendMessagesHandmade, MaillingDetailView

# from catalog.apps import CatalogConfig
# from maiiling.views import (RecipientListView, RecipientDetailView, RecipientCreateView, RecipientUpdateView,
#                             RecipientDeleteView, MailListView, MailDetailView, MailCreateView, MailUpdateView,
#                             MailDeleteView, HomeListView)

# app_name = CatalogConfig.name
app_name = 'mailling'

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('sendmessages/', SendMessagesHandmade.as_view(), name='send_handmade'),
    path('detail/', MaillingDetailView.as_view(), name='mailling_detail'),

    # path('recipient/', RecipientListView.as_view(), name='recipient'),
    # path('recipient/<int:pk>/', RecipientDetailView.as_view(), name='recipient_detail'),
    # path('recipient/create/', RecipientCreateView.as_view(), name='recipient_create'),
    # path('recipient/<int:pk>/update/', RecipientUpdateView.as_view(), name='recipient_update'),
    # path('recipient/<int:pk>/delete/', RecipientDeleteView.as_view(), name='recipient_delete'),
    #
    # path('mail/', MailListView.as_view(), name='mail'),
    # path('mail/<int:pk>/', MailDetailView.as_view(), name='mail_detail'),
    # path('mail/create/', MailCreateView.as_view(), name='mail_create'),
    # path('mail/<int:pk>/update/', MailUpdateView.as_view(), name='mail_update'),
    # path('mail/<int:pk>/delete', MailDeleteView.as_view(), name='mail_delete'),
]
