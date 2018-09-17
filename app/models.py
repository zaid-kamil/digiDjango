from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class TaskRequest(models.Model):
    
    lang_option= [
        ('Android','android'),
        ('Python','python'),
        ('Other','other'),
    ]
    
    subject = models.CharField(max_length=255, blank=False, null=False,help_text="Please provide a brief subject")
    description = models.TextField(max_length=3000,blank=False,null=False,help_text="Please describe the task")
    created = models.DateField( auto_now_add=True)
    language = models.CharField(max_length=30,choices=lang_option, blank=False, null=False,default="other")

    class Meta:
        """Meta definition for Task."""

        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        """Unicode representation of Task."""
        return self.subject

    def __repr__(self):
        """Unicode representation of Task."""
        self.subject

class Profile(models.Model):
    """Model definition for Profile."""

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_pic = models.ImageField( upload_to=f'profiles', max_length=250,unique=True)
    created = models.DateField(auto_now_add=True)

    class Meta:
        """Meta definition for Profile."""

        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        """Unicode representation of Profile."""
        return self.user.username

    def __repr__(self):
        """Unicode representation of Profile."""
        self.user.username

    def image_tag(self):
        return mark_safe(f'<img src="{self.profile_pic.url}"  height="64" />')

    image_tag.short_description = 'Image'

