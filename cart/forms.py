from django import forms


class ShareCartForm(forms.Form):
    username = forms.CharField(label='Username', required=False)
    email = forms.EmailField(label='Email', required=False)

    def clean(self):
        cleaned_data = super(ShareCartForm, self).clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')

        if not username or not email:
            raise forms.ValidationError('Please fill in one of the fields.')
        if username and email:
            raise forms.ValidationError('Please only use one of the options.')

        return cleaned_data
