from django.forms import ModelForm

from .models import Group, Groupmember


class GroupForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Naam'].widget.attrs.update(
            {
                'class': 'border-2 rounded border-gray-400 bg-nord6 focus:outline-none focus:border-green-400 text-gray-700'})

    class Meta:
        model = Group
        fields = ['Naam']


class GroupmemberForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Naam'].widget.attrs.update({'class': ''})
        self.fields['Group'].widget.attrs.update({'class': ''})
        self.fields['Brakcounter'].widget.attrs.update({'class': ''})

    class Meta:
        model = Groupmember
        fields = ['Naam', 'Group', 'Brakcounter']
