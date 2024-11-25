from django import forms
from . import models, parser_manas

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('manas', 'manas'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = [
            'media_type',
        ]

    def parser_data(self):
        if self.data['media_type'] == 'manas':
            manas_pars = parser_manas.parsing()
            for i in manas_pars:
                models.Manas. objects.create(**i)