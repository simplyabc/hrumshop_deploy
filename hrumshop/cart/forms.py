from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput, Textarea
from .models import Order


class OrderAddForm(ModelForm):
    class Meta:
        model = Order
        fields = ['id', 'name', 'phone', 'address', 'comments']
        widgets = {
            'phone': TextInput(attrs={'type': 'tel'}),
            'comments': Textarea(attrs={'cols': 60, 'rows': 10})
        }

    def clean_phone(self):
        phone = ''.join((i for i in self.cleaned_data['phone'] if i.isnumeric()))
        if len(phone) > 11:
            raise ValidationError('Длина номера телефона превышает 11 символов')
        return phone