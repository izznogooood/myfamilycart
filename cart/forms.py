from django import forms


class ShareCartForm(forms.Form):
    username = forms.CharField(label='Username', required=False)
    email = forms.EmailField(label='Email', required=False)

    def clean(self):
        cleaned_data = super(ShareCartForm, self).clean()

        if not cleaned_data.get('username') and not cleaned_data.get('email'):
            raise forms.ValidationError('Please fill in one of the fields.')
        if cleaned_data.get('username') and cleaned_data.get('email'):
            raise forms.ValidationError('Please only use one of the options.')

        return cleaned_data
