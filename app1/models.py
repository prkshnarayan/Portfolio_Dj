from django.db import models

# Create your models here.
from django.utils import timezone


class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    submission_date = models.DateTimeField(default=timezone.now)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    class Meta:
        db_table = 'email_messages'

    def __str__(self):
        return f"Contact from {self.name} ({self.email})"

