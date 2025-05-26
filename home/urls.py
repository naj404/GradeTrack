from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),                      
    path('home/', views.home_view, name='home'),              
    path('admin/', views.fetch_reports_view, name='custom_admin'),  
    path('login/', views.login_view, name='login'),         
    path('admin-login/', views.admin_login_view, name='admin_login'), 
    path('submit-report/', views.submit_report_view, name='submit_report'), 
    path('update-grade/', views.update_grade_view, name='update_grade'),
    path("history/", views.history_view, name="history"),

]