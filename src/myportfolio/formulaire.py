from django import forms
from myportfolio.models import PorfolioMessage


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = PorfolioMessage
        fields = ["nom", "email", "message", ]

