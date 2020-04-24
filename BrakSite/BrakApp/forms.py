from django.forms import ModelForm

from .models import Huis, Huisgenoot


class HuisForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Naam'].widget.attrs.update(
            {'class': 'border-2 rounded border-gray-400 focus:outline-none focus:border-green-200 text-gray-700'})

    class Meta:
        model = Huis
        fields = ['Naam']


class HuisgenootForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.fields['Naam'].widget.attr.update({'class': ''})
        self.fields['Huis'].widget.attr.update({'class': ''})
        self.fields['Laatst_brak'].widget.attr.update({'class': ''})

    class Meta:
        model = Huisgenoot
        fields = ['Naam', 'Huis', 'Laatst_brak']
