from django import forms

# PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
PRODUCT_QUANTITY_CHOICES = [(1, '1'), (9, '9'), (11, '11'), (15, '15'), (21, '21'), (33, '33'), (50,'50'), (100,'100')]


class CartAddProductForm(forms.Form):
    """
    quantity: позволяет пользователю выбрать количество между 1-20. Мы используем поле
    update: TypedChoiceField с coerce=int для преобразования ввода в целое число.
    """
    quantity = forms.TypedChoiceField(label='Количество цветов в букете', choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

