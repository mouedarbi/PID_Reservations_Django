from django.urls import path
from .admin_views import AdminDashboardView, admin_home

app_name = 'catalogue_admin'

urlpatterns = [
    path('dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('', admin_home, name='admin_home'),
]