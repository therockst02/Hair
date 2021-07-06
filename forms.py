from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from .models import Appuntamenti
import datetime
from django.forms.widgets import SelectDateWidget

ORARI = (
            ('07:00:00', '07:00:00'),
            ('07:30:00', '07:30:00'),
            ('08:00:00', '08:00:00'),
            ('08:30:00', '08:30:00'),
            ('09:00:00', '09:00:00'),
            ('09:30:00', '09:30:00'),
            ('10:00:00', '10:00:00'),
            ('10:30:00', '10:30:00'),
            ('11:00:00', '11:00:00'),
            ('11:30:00', '11:30:00'),
            ('12:00:00', '12:00:00'),
            ('12:30:00', '12:30:00'),
            ('01:00:00', '01:00:00'),
            ('01:30:00', '01:30:00'),
            ('03:00:00', '03:00:00'),
            ('03:30:00', '03:30:00'),
            ('04:00:00', '04:00:00'),
            ('04:30:00', '04:30:00'),
            ('05:00:00', '05:00:00'),
            ('05:30:00', '05:30:00'),
            ('06:00:00', '06:00:00'),
            ('06:30:00', '06:30:00'),
            ('07:00:00', '07:00:00'),
            ('07:30:00', '07:30:00'),
            ('08:00:00', '08:00:00'),
            ('08:30:00', '08:30:00'),
    )

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))



class AppuntamentiForm(forms.ModelForm):
    class Meta:
        model = Appuntamenti
        fields = ['Id_Trattamento', 'Id_Dipendente', 'Data', 'Ora']
    Ora = forms.TimeField(widget = forms.Select(choices = ORARI))
    Data = forms.DateField(widget = forms.SelectDateWidget(attrs={'style': 'display: inline-block; width: 33%;'}))



