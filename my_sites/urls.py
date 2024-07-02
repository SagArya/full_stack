from django.urls import path
from .views import *
urlpatterns = [
    path('all_sites/', all_sites, name='all_sites'),
    path('add_site/', add_site, name='add_site'),
    path('site_detail/<int:site_id>/', site_detail, name='site_detail'),
    path('add_material_report/<int:site_id>/', add_material_report, name='add_material_report'),
    path('add_machinery_report/<int:site_id>/', add_machinery_report, name='add_machinery_report'),
    path('add_site_expense_report/<int:site_id>/', add_site_expense_report, name='add_site_expense_report'),
    path('site_reports/<int:site_id>/', site_reports, name='site_reports'),
    path('view_material_report/<int:report_id>/', view_material_report, name='view_material_report'),
    path('view_machinery_report/<int:report_id>/', view_machinery_report, name='view_machinery_report'),
    path('view_site_expense_report/<int:report_id>/', view_site_expense_report, name='view_site_expense_report'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
]