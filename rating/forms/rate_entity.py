from django import forms

from rating.models.legal_entity import LegalEntity as LegalEntityModel


class RateEntityForm(forms.ModelForm):
    class Meta:
        model = LegalEntityModel
        fields = ['rating', 'comment']

    rating = forms.IntegerField(required=True, max_value=100, min_value=0)

    # TODO add widgets
    # widgets = {
    #   'rating': forms.IntegerField(attrs={'class': 'form-control'}),
    #   'comment': forms.Textarea(attrs={'class': 'form-control'})
    # }
