from contact.models import Contact
from django.contrib import admin
from django import forms


class ContactAdminForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 10}))
    class Meta:
        model = Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('topic', 'message', 'sender', 'created_at')
    form = ContactAdminForm

admin.site.register(Contact, ContactAdmin)