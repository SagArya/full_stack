from django.db import models
from my_sites.models import Site

class Worker(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    daily_rate = models.DecimalField(max_digits=10, decimal_places=2)  # Daily wage rate
    contact_info = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# class Site(models.Model):
#     name = models.CharField(max_length=100)
#     location = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

class Attendance(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField()

    def __str__(self):
        return f"{self.worker.name} at {self.site.name} on {self.date}"

class AdvancePayment(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.worker.name} - {self.amount}"

class Salary(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    week_ending = models.DateField()
    total_days_worked = models.IntegerField()
    total_salary = models.DecimalField(max_digits=10, decimal_places=2)
    advances_deducted = models.DecimalField(max_digits=10, decimal_places=2)
    net_salary = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.worker.name} - {self.net_salary} - {'Paid' if self.paid else 'Unpaid'}"