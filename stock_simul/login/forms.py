from django.forms import ModelForm
from .models import userData

class registerform(ModelForm):

    class Meta:
        model = userData
        fields = ['account','password','secPassword']

    def clean(self):#密碼不同則創建失敗
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        secPassword = cleaned_data.get('secPassword')

        if password and secPassword and password != secPassword:
            self.add_error('secPassword', 'The two password fields must match.')

        return cleaned_data
    
    def clean_account(self):#帳號名稱相同則無法創建
        account = self.cleaned_data.get('account')
        if userData.objects.filter(account=account).exists():
            self.add_error('account', 'account has already exist')
        return account


class loginform(ModelForm):
    class Meta:
        model = userData
        fields = ['account','password']
