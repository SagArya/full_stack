from django.db import models
from django.contrib.auth.models import User

class Site(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    start_date = models.DateField()
    picture = models.ImageField(upload_to='site_pictures/', null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class MaterialReport(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    date = models.DateTimeField()
    material_type = models.CharField(max_length=20)
    supplier_name = models.CharField(max_length=50)
    quantity = models.FloatField()
    unit = models.CharField(max_length=10, blank=True, null=True)
    vehicle_no = models.CharField(max_length=20)
    challan_no = models.CharField(max_length=20)
    material_image = models.ImageField(upload_to='material_reports/', blank=True, null=True)
    remark = models.TextField(max_length=500)


    def __str__(self):
        return f"Material Report for {self.site.name} on {self.date}"

class MachineryReport(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    date = models.DateTimeField()
    machine_type = models.CharField(max_length=50)
    supplier_name = models.CharField(max_length=50)
    registration_no = models.CharField(max_length=20)
    hours_worked = models.DurationField()
    challan_no = models.CharField(max_length=20)
    machinary_image = models.ImageField(upload_to='machinary_reports/', blank=True, null=True)
    remark = models.TextField(max_length=500)

    def __str__(self):
        return f"Machinery Report for {self.site.name} on {self.date}"
    
class SiteExpenseReport(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    date = models.DateTimeField()
    reason = models.CharField(max_length=400)
    expense_image = models.ImageField(upload_to='expense_reports/', blank=True, null=True)
    amount = models.IntegerField()

    def __str__(self):
        return f"Site Expense Report for {self.site.name} on {self.date}"