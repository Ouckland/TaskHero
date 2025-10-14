from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils import timezone

User = get_user_model()
# Create your models here.
class StatusChoices(models.TextChoices):
    to_do = 'TD', 'To-Do'
    in_progress = 'IP', 'In-Progress'
    completed = 'CPD', 'Completed'
class PriorityChoices(models.TextChoices):
    low = 'LW', 'Low'
    medium = 'MD', 'Medium'
    high = 'HG', 'High'

class TaskModel(models.Model):
    def validate_due_date(date):
        current_date = timezone.now().date()
        if date < current_date:
            raise ValidationError('Due date cannot be in the past!')

    title = models.CharField(max_length=255)
    description = models.CharField()
    due_date = models.DateField(validators=[validate_due_date], default=timezone.now().date())
    status = models.CharField(choices=StatusChoices.choices, max_length=3, default=StatusChoices.to_do)
    priority = models.CharField(choices=PriorityChoices.choices, max_length=2, default=PriorityChoices.low)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'{self.title} - {self.due_date}'