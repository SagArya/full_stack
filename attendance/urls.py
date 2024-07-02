from django.urls import path
from . import views
from .views import edit_worker, delete_worker

urlpatterns = [
    path('', views.worker_list, name='worker_list'),
    path('add_worker/', views.add_worker, name='add_worker'),
    path('workers/edit/<int:pk>/', edit_worker, name='edit_worker'),
    path('workers/delete/<int:pk>/', delete_worker, name='delete_worker'),
    path('add_site/', views.add_site, name='add_site'),
    path('sites/', views.site_list, name='site_list'),
    path('record_attendance/', views.record_attendance, name='record_attendance'),
    path('record_advance_payment/', views.record_advance_payment, name='record_advance_payment'),
    path('calculate_salary/', views.calculate_salary, name='calculate_salary'),
]
