from django import forms
from .models import Employee

class AddEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['Empid', 'Name', 'Gender', 'Email', 'Address', 'Contact', 'Department', 'Salary']
        widgets = {
            'Empid': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Employee ID',
                'min': '1'
            }),
            'Name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Full Name'
            }),
            'Gender': forms.Select(attrs={
                'class': 'form-control'
            }),
            'Email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Email Address'
            }),
            'Address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Address',
                'rows': 3,
                'maxlength': 200  # Increased for longer addresses
            }),
            'Contact': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Contact Number',
                'type': 'tel'  # For mobile-friendly keyboard
            }),
            'Department': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Department'
            }),
            'Salary': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Salary',
                'step': '0.01'
            }),
        }

def clean_salary(self):
    salary = self.cleaned_data.get('Salary')
    if salary is None or salary <= 0:
        raise forms.ValidationError('Salary must be a positive number.')
    return salary

