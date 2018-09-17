from .models import TaskRequest
from django.forms import ModelForm


class TaskRequestForm(ModelForm):
    """Form definition for TaskRequest."""
    class Meta:
        """Meta definition for TaskRequestform."""
        model = TaskRequest
        fields = ('subject','description','language')



