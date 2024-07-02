# views.py in my_sites app
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import Site, MaterialReport, MachineryReport, SiteExpenseReport
from django.utils import timezone
from .forms import SiteForm, MaterialReportForm, MachineryReportForm, SiteExpenseReportForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

@login_required(login_url='/login/')
def all_sites(request):
    sites = Site.objects.all()
    return render(request, 'my_sites/all_sites.html', {'sites': sites})

@login_required
def add_site(request):
    if request.method == 'POST':
        form = SiteForm(request.POST, request.FILES)
        if form.is_valid():
            site = form.save(commit=False)
            site.created_by = request.user
            site.save()
            return redirect('site_detail', site_id=site.id)
    else:
        form = SiteForm()
    return render(request, 'my_sites/add_site.html', {'form': form})

@login_required
def site_detail(request, site_id):
    site = Site.objects.get(pk=site_id)
    return render(request, 'my_sites/site_detail.html', {'site': site})

# #@login_required
# def add_material_report(request, site_id):
#     site = Site.objects.get(pk=site_id)
#     if request.method == 'POST':
#         form = MaterialReportForm(request.POST)
#         if form.is_valid():
#             report = form.save(commit=False)
#             report.site = site
#             report.save()
#             return redirect('site_detail', site_id=site.id)
#     else:
#         form = MaterialReportForm()
#     return render(request, 'my_sites/add_report.html', {'form': form, 'site': site, 'report_type': 'Material Report'})

@login_required
def add_material_report(request, site_id):
    site = get_object_or_404(Site, pk=site_id)

    if request.method == 'POST':
        date = request.POST.get('date')
        material_type = request.POST.get('material_type')
        supplier_name = request.POST.get('supplier_name')
        quantity = request.POST.get('quantity')
        vehicle_no = request.POST.get('vehicle_no')
        challan_no = request.POST.get('challan_no')
        material_image = request.FILES.get('material_image') 
        remark = request.POST.get('remark')

        report = MaterialReport.objects.create(
            site=site, date=date, material_type=material_type,
            supplier_name=supplier_name, quantity=quantity,
            vehicle_no=vehicle_no, challan_no=challan_no, remark=remark, material_image=material_image,
        )

        # Fetch material reports after adding a new report
        material_reports = MaterialReport.objects.filter(site=site).order_by('-date')

        return render(request, 'my_sites/add_material_report.html', {
            'site': site,
            'report_type': 'Material Report',
            'material_reports': material_reports,
        })

    # Fetch material reports for the initial rendering
    material_reports = MaterialReport.objects.filter(site=site).order_by('-date')
    
    return render(request, 'my_sites/add_material_report.html', {
        'site': site,
        'report_type': 'Material Report',
        'material_reports': material_reports,
    })

# #@login_required
# def add_machinery_report(request, site_id):
#     site = Site.objects.get(pk=site_id)
#     if request.method == 'POST':
#         form = MachineryReportForm(request.POST)
#         if form.is_valid():
#             report = form.save(commit=False)
#             report.site = site
#             report.save()
#             return redirect('site_detail', site_id=site.id)
#     else:
#         form = MachineryReportForm()
#     return render(request, 'my_sites/add_report.html', {'form': form, 'site': site, 'report_type': 'Machinary Report'})

@login_required
def add_machinery_report(request, site_id):
    site = get_object_or_404(Site, pk=site_id)

    if request.method == 'POST':
        form = MachineryReportForm(request.POST)
        if form.is_valid():
            machinery_report = form.save(commit=False)
            machinery_report.site = site
            machinery_report.hours_worked = calculate_duration(
                form.cleaned_data['start_time'], form.cleaned_data['end_time']
            )
            machinery_report.save()

            # Fetch machinery reports after adding a new report
            machinery_reports = MachineryReport.objects.filter(site=site).order_by('-date')

            return render(request, 'my_sites/add_machinery_report.html', {
                'site': site,
                'report_type': 'Machinery Report',
                'machinery_reports': machinery_reports,
            })

    # Fetch machinery reports for the initial rendering
    machinery_reports = MachineryReport.objects.filter(site=site).order_by('-date')
    form = MachineryReportForm()

    return render(request, 'my_sites/add_machinery_report.html', {
        'site': site,
        'report_type': 'Machinery Report',
        'machinery_reports': machinery_reports,
        'form': form,
    })

def calculate_duration(start_time, end_time):
    """
    Calculate the duration in hours between start_time and end_time.
    """
    duration = end_time - start_time
    duration_hours = duration.total_seconds() / 3600
    return duration_hours

#@login_required
# def add_site_expense_report(request, site_id):
#     site = Site.objects.get(pk=site_id)
#     if request.method == 'POST':
#         form = SiteExpenseReportForm(request.POST)
#         if form.is_valid():
#             report = form.save(commit=False)
#             report.site = site
#             report.save()
#             return redirect('site_detail', site_id=site.id)
#     else:
#         form = SiteExpenseReportForm()
#     return render(request, 'my_sites/add_report.html', {'form': form, 'site': site, 'report_type': 'Site Expense Report'})

@login_required
def add_site_expense_report(request, site_id):
    site = get_object_or_404(Site, pk=site_id)

    if request.method == 'POST':
        date = request.POST.get('date')
        reason = request.POST.get('reason')
        amount = request.POST.get('amount')

        report = SiteExpenseReport.objects.create(site=site, date=date, reason=reason, amount=amount)

        # Fetch site expense reports after adding a new report
        site_expense_reports = SiteExpenseReport.objects.filter(site=site).order_by('-date')

        return render(request, 'my_sites/add_site_expense_report.html', {
            'site': site,
            'report_type': 'Site Expense Report',
            'site_expense_reports': site_expense_reports,
        })

    # Fetch site expense reports for the initial rendering
    site_expense_reports = SiteExpenseReport.objects.filter(site=site).order_by('-date')

    return render(request, 'my_sites/add_site_expense_report.html', {
        'site': site,
        'report_type': 'Site Expense Report',
        'site_expense_reports': site_expense_reports,
    })

# Similar views for machinery and site expense reports
# ...

@login_required
def site_reports(request, site_id):
    site = Site.objects.get(pk=site_id)
    material_reports = MaterialReport.objects.filter(site=site)
    machinery_reports = MachineryReport.objects.filter(site=site)
    site_expense_reports = SiteExpenseReport.objects.filter(site=site)
    return render(request, 'my_sites/site_reports.html', {
        'site': site,
        'material_reports': material_reports,
        'machinery_reports': machinery_reports,
        'site_expense_reports': site_expense_reports,
    })

def view_material_report(request, report_id):
    material_report = get_object_or_404(MaterialReport, pk=report_id)
    return render(request, 'my_sites/view_material_report.html', {'material_report': material_report})

def view_machinery_report(request, report_id):
    machinery_report = get_object_or_404(MachineryReport, pk=report_id)
    return render(request, 'my_sites/view_machinery_report.html', {'machinery_report': machinery_report})

def view_site_expense_report(request, report_id):
    site_expense_report = get_object_or_404(SiteExpenseReport, pk=report_id)
    return render(request, 'my_sites/view_site_expense_report.html', {'site_expense_report': site_expense_report})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")
            return redirect('home')
        else:
            messages.error(request, "Invalid login credentials.")

    return render(request, 'my_sites/login.html')

def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')