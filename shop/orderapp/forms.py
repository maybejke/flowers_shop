from django import forms

from orderapp.models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'email', 'address', 'phone_number', 'comment']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иван'}),
            'address': forms.TextInput(attrs={'class': 'form-control',
                                              'placeholder': 'ул. Красная, д. 1, кв. 4, под. 4, эт. 3'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ivan@mail.ru'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '89171112233'}),
            'comment': forms.Textarea(attrs={'class': 'form-control',
                                             'placeholder': 'Дополнительная информация к заказу'})
        }


class OrderGiftCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'gift_name', 'address', 'gift_phone_number', 'phone_number', 'email', 'comment']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}),
            'gift_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя получателя'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' Адресс получателя'}),
            'gift_phone_number': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Мобильный телефон получателя'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваш мобильный'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваш e-mail'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Комментарии к заказу'}),
        }
