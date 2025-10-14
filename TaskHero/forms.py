from django import forms
from .models import TaskModel

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = [
            'title', 'description', 'due_date', 'status', 'priority',
        ]
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea()
                }
class SearchForm(forms.Form):
    title = forms.CharField(required=False, max_length=255,  widget=forms.TextInput)

# class FilterForm(forms.Form):
#     filter_by = forms.ChoiceField(choices=)