from django import forms


class ContactForm(forms.Form):
    sender_name = forms.CharField(label="Your Name", required=True)
    sender_email = forms.EmailField(label="Your Email", required=True)
    sender_message = forms.CharField(
        label="Your Message",
        required=True,
        widget=forms.Textarea
    )
