from django import forms

TOPIC_CHOICES = (
    ('general', 'General enquiry'),
    ('bug', 'Bug report'),
    ('suggestion', 'Suggestion'),
)

class ContactForm(forms.Form):
    topic = forms.ChoiceField(choices=TOPIC_CHOICES)
    # add length validation here
    message = forms.CharField(widget=forms.Textarea(),
        initial="Replace with your feedback",
        max_length=100)
    sender = forms.EmailField(required=False)


    # clean_<field> automatically picked up by Django
    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        return message