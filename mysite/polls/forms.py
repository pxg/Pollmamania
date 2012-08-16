from django import forms

TOPIC_CHOICES = (
    ('general', 'General enquiry'),
    ('bug', 'Bug report'),
    ('suggestion', 'Suggestion'),
)

class PollForm(forms.Form):
    question = forms.CharField(widget=forms.Textarea(),
        max_length=100)


    def clean_question(self):
        question = self.cleaned_data['question']
        #TODO: look and check for duplicate questions here

        #if num_words < 4:
        #    raise forms.ValidationError("Not enough words!")
        return question

class ChoiceForm(forms.Form):
    choice_text = forms.CharField()