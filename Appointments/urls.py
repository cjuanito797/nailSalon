from django.urls import path, re_path

from . import views

app_name = 'appointments'

urlpatterns = [
    path('services/', views.service_list, name='service_list'),
    path('services/<slug:category_slug>/', views.service_list, name='service_list_by_category'),
    path('services/<int:id>/<slug:slug>/', views.service_detail, name='service_detail'),
    path('create/', views.appointment_create, name='appointment_create'),
    path('schedule/<int:pk>/<int:date>/', views.scheduleWithTech, name='schedule'),
    path('schedule/-1/<int:date>/', views.scheduleWithNoneTech, name='scheduleNone'),
    path('confirm', views.confirmAppointment, name='confirm'),
    path('e-mailConfirm/', views.index, name='confirmation'),
    path('delete/<int:id>/', views.deleteAppointment, name='delete'),
    path('reschedule/<int:id>/<str:date>/', views.rescheduleAppointment, name='reschedule'),
    path('schedule/<str:date>/', views.scheduleWithNoneTech, name='schedule_none_tech'),
    path('selectCustomer/', views.selectCustomer, name='select_customer'),
    path('confirm/<int:id>/', views.manager_confirmation, name='manager_confirmation'),

]
