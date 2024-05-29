from django.forms import ModelForm
from .models import userData

class userform(ModelForm):

    class Meta:
        model = userData
        fields = ['account','password','secPassword']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        secPassword = cleaned_data.get('secPassword')

        if password and secPassword and password != secPassword:
            self.add_error('secPassword', 'The two password fields must match.')

        return cleaned_data
    
