from django.db import models

# Create your models here.
class accountsModel(models.Model):
    email = models.CharField(max_length=100, help_text='Enter your email address')
    name = models.CharField(max_length=200, null=True, unique=True)
    password = models.CharField(max_length=200, null=True)
    address = models.TextField(max_length=800, null=True)
    dob = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)

    def __str___(self):
        return self.name

class new_passwordsModel(models.Model):
    website = models.CharField(max_length=200, blank=False, null=True)
    username = models.CharField(max_length=200, blank=False, null=True)
    password = models.CharField(max_length=200, blank=False, null=True)
    user_email = models.CharField(max_length=100)

    def __str__(self):
        return

    def __unicode__(self):
        return 