from django import forms
from .models import Worker, Attendance, AdvancePayment, Site

class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = '__all__'

class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = '__all__'

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'

class AdvancePaymentForm(forms.ModelForm):
    class Meta:
        model = AdvancePayment
        fields = '__all__'
