from django import forms
from .models import Product, Category


class ProductForm(form.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(sef, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].chices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
