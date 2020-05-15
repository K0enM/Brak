from django.forms import ModelForm, SelectDateWidget

from . import helpers
from .models import Group, Groupmember, BRAK


class GroupForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        style = helpers.get_form_class(self.__class__.__name__)
        self.fields['Naam'].widget.attrs.update(
            {
                'class': style})

    class Meta:
        model = Group
        fields = ['Naam']


class GroupmemberForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        style = helpers.get_form_class(self.__class__.__name__)
        self.fields['Naam'].widget.attrs.update({
            'class': style})
        self.fields['Group'].widget.attrs.update({
            'class': style})
        self.fields['Group'].disabled = True
        self.fields['Brakcounter'].widget.attrs.update({
            'class': style})

    class Meta:
        model = Groupmember
        fields = ['Naam', 'Group', 'Brakcounter']


class BrakForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        style = helpers.get_form_class(self.__class__.__name__)
        self.fields['Groupmember'].widget.attrs.update({'class': style})
        self.fields['Datum'].widget = SelectDateWidget()
        self.fields['Datum'].widget.attrs.update({'class': style})
        self.fields['Brak_level'].widget.attrs.update({'class': style})

    class Meta:
        model = BRAK
        fields = ['Groupmember', 'Datum', 'Brak_level']
