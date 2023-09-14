from django import forms

from university import models
from university.models import Student, Department, Faculty, Group, AbsenceLog, Subject


class addStudent(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'surname', 'group', 'birthday', 'joined', 'email']


class Ambion(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'shortname', 'manager', 'teachers']
        widgets = {
            'manager': forms.Select(attrs={'class': 'select2_single form-control'}),
            'teachers': forms.SelectMultiple(attrs={'class': 'select2_multiple form-control'}),
            'shortname': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }


class Fakultet(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['name', 'shortname', 'dean']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'shortname': forms.TextInput(attrs={'class': 'form-control'}),
            'dean': forms.Select(attrs={'class': 'select2_single form-control'})
        }


class Group(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'profession', 'created', 'lecturers']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'profession': forms.Select(attrs={'class': 'select2_single form-control'}),
            'created': forms.DateInput(attrs={'class': 'form-control'}),
            'lecturers': forms.SelectMultiple(attrs={'class': 'select2_multiple form-control'}),
        }


class Matyan(forms.ModelForm):
    class Meta:
        model = AbsenceLog
        fields = ['student', 'group', 'loose', 'minute', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'student': forms.Select(attrs={'class': 'select2_single form-control'}),
            'group': forms.Select(attrs={'class': 'select2_single form-control'}),
            'minute': forms.NumberInput(attrs={'class': 'form-control'}),
            'loose': forms.CheckboxInput(attrs={'class': 'form-control'})
        }


class Points(forms.ModelForm):
    class Meta:
        model = models.Points
        fields = ['value', 'student', 'type', 'exam']
        widgets = {
            'student': forms.Select(attrs={'class': 'select2_single form-control'}),
            'exam': forms.Select(attrs={'class': 'select2_single form-control'}),
            'type': forms.Select(attrs={'class': 'select2_single form-control'}),
            'value': forms.NumberInput(attrs={'class': 'form-control'})
        }


class Profession(forms.ModelForm):
    class Meta:
        model = models.Profession
        fields = ['name', 'faculty', 'years', 'remote', 'subjects']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'faculty': forms.Select(attrs={'class': 'select2_single form-control'}),
            'subjects': forms.SelectMultiple(attrs={'class': 'select2_multiple form-control'}),
            'years': forms.NumberInput(attrs={'class': 'form-control'}),
            'remote': forms.CheckboxInput(attrs={'class': 'form-control'})
        }


class Staff(forms.ModelForm):
    class Meta:
        model = models.Staff
        fields = ['fullname', 'works_since', 'type']
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'select2_single form-control'}),
            'works_since': forms.DateInput(attrs={'class': 'form-control'})
        }


class Student(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'surname', 'group', 'birthday', 'joined', 'email', 'phone', 'tuition_fee',
                  'state_order', 'image']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'group': forms.Select(attrs={'class': 'select2_single form-control'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control'}),
            'joined': forms.DateInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'tuition_fee': forms.NumberInput(attrs={'class': 'form-control'}),
            'state_order': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }


class Subject(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'lecturers', 'course', 'lessons']
        widgets = {
            'lecturers': forms.SelectMultiple(attrs={'class': 'select2_multiple form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'course': forms.NumberInput(attrs={'class': 'form-control'}),
            'lessons': forms.NumberInput(attrs={'class': 'form-control'})
        }


class Exam(forms.ModelForm):
    class Meta:
        model = models.Exam
        fields = ['subject', 'group', 'type', 'lecturer']
        widgets = {
            'subject': forms.Select(attrs={'class': 'select2_single form-control'}),
            'group': forms.Select(attrs={'class': 'select2_single form-control'}),
            'type': forms.Select(attrs={'class': 'select2_single form-control'}),
            'lecturer': forms.Select(attrs={'class': 'select2_single form-control'}),
        }
