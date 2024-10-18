from django import forms

class MyForm(forms.Form):
    name = forms.CharField( max_length=100, required=True, label='Enter your first name')
    last_name = forms.CharField( max_length=100, required=True, 
                    widget=forms.TextInput(attrs={'placeholder': 'Your last name'}))
