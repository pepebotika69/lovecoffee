from django import forms

from judge.models.judge import Judge as JudgeModel


class JudgeEditForm(forms.ModelForm):
    class Meta:
        model = JudgeModel
        fields = ['reputation']

        reputation = forms.IntegerField(required=True, max_value=100, min_value=0)
