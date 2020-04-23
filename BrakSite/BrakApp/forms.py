from django.forms import ModelForm

from .models import Huis


class HuisForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Naam'].widget.attrs.update(
            {'class': 'border-2 rounded border-gray-400 focus:outline-none focus:border-green-200 text-gray-700'})

    class Meta:
        model = Huis
        fields = ['Naam']
