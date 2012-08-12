from django.db import models

class Contact(models.Model):
    topic = models.CharField(max_length=100) # match form validation
    message = models.TextField(max_length=1000)
    sender = models.CharField(max_length=100)

    # automatic system fields
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        # NOTE: Maybe feedback would have been a better class name
        verbose_name_plural = "Messages"