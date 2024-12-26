from django import forms

class FeedbackForm(forms.Form):
    username = forms.CharField(max_length=100, label='User Name')
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label='Confirm Password')
    phone_number = forms.CharField(max_length=15, label='Phone Number')
    feedback_message = forms.CharField(widget=forms.Textarea, label='Feedback Message')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        phone_number = cleaned_data.get("phone_number")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")

        if phone_number and not phone_number.isdigit():
            self.add_error('phone_number', "Phone number must contain only digits.")
        if len(phone_number) < 10:
            self.add_error('phone_number', "Phone number must be at least 10 digits.")
