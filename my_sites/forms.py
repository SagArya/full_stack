from django import forms
from .models import Site, MaterialReport, MachineryReport, SiteExpenseReport

class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['name', 'location', 'start_date', 'picture']

class MaterialReportForm(forms.ModelForm):
    class Meta:
        model = MaterialReport
        fields = ['date', 'material_type','supplier_name','quantity','vehicle_no','challan_no','remark']

class MachineryReportForm(forms.ModelForm):
    class Meta:
        model = MachineryReport
        fields = ['date', 'machine_type','supplier_name','registration_no','hours_worked','challan_no','remark']

class SiteExpenseReportForm(forms.ModelForm):
    class Meta:
        model = SiteExpenseReport
        fields = ['date', 'reason','amount']
