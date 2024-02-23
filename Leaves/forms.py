
from django import forms
from django.core.exceptions import ValidationError
from .models import Leave

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = ['Emp_id','start_date','end_date']

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if start_date and end_date and start_date >= end_date :
            raise ValidationError("Error :- please confirm the correct dates")

        return cleaned_data
