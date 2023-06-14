from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField, TextInput, Textarea
from .models import Order

#validators=[RegexValidator(regex = r"^\+?1?\d{8,15}$")]

class OrderAddForm(ModelForm):
    class Meta:
        model = Order
        fields = ['id', 'name', 'phone', 'address', 'comments']
        widgets = {
            'phone': TextInput(attrs={'type': 'tel', 'pattern': '[0-9]{3}-[0-9]{2}-[0-9]{3}'}),
            'comments': Textarea(attrs={'cols': 60, 'rows': 10})
        }

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if len(phone) > 11:
            raise ValidationError('Длина номера телефона превышает 11 символов')

        return phone