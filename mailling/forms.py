from django.forms import BooleanField
from django import forms
from mailling.models import Mail, Recipient, Mailling


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"

class GoMail(forms.ModelForm):
    class Meta:
        model = Mail
        fields = ['theme', 'body_mail']

class RecipientForm(forms.ModelForm):
    class Meta:
        model = Recipient
        fields = ['email', 'full_name', 'comment']

    def __init__(self, *args, **kwargs):
        super(RecipientForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите email'
        })
        self.fields['full_name'].widget.attrs.update({
            'class': 'form-control ',
            'placeholder': 'Введите ФИО'
        })
        self.fields['comment'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Добавьте комментарий'})

class MailForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields = ['theme','body_mail']

    def __init__(self, *args, **kwargs):
        super(MailForm, self).__init__(*args, **kwargs)
        self.fields['theme'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите тему письма'
        })
        self.fields['body_mail'].widget.attrs.update({
            'class': 'form-control ',
            'placeholder': 'Ваше сообщение: ФИО'
        })

    # def clean(self):
    #     cleaned_data = super().clean()
    #     name = cleaned_data.get('name').lower()
    #     description = cleaned_data.get('description').lower()
    #     for spam in SPAMS:
    #         if spam in name:
    #             self.add_error('name', f'Имя не может содержать запрещённые слова. Вы ввели: {spam}')
    #         if spam in description:
    #             self.add_error('description', f'Описание не может содержать запрещённые слова. Вы ввели: {spam}')


class MaillingForm(forms.ModelForm):
    class Meta:
        model = Mailling
        exclude = ['startDt', 'endDt']

    def __init__(self, *args, **kwargs):
        super(MaillingForm, self).__init__(*args, **kwargs)

        self.fields['my_field'].widget.attrs.update({
            'class': 'form-control ',
            'placeholder': '#'
        })
        self.fields['mail'].widget.attrs.update({
            'class': 'form-control ',
            'placeholder': 'Ваше сообщение:'
        })
        self.fields['recipient'].widget.attrs.update({
            'class': 'form-control ',
            'placeholder': 'Получатель:'
        })
