from contact.models import Contact
from django.contrib import admin
from django import forms


# custom textarea form example
class ContactAdminForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 10}))
    class Meta:
        model = Contact


# fields to display in the table view
class ContactAdmin(admin.ModelAdmin):
    list_display = ('topic', 'message', 'sender', 'created_at')
    form = ContactAdminForm

    # don't allow addition in CMS
    def has_add_permission(self, request):
        return False

    # Remove the delete Admin Action for this Model
    def has_delete_permission(self, request, obj=None):
        return False

    #Return nothing to make sure user can't update any data
    def save_model(self, request, obj, form, change):
        pass

admin.site.register(Contact, ContactAdmin)