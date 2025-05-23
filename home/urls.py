from django.urls import path
from . import views
from .views import home_view
from .views import index, home_view
from .views import custom_admin_view

urlpatterns = [
    path('', index, name='index'),           # for /
    path('home/', home_view, name='home'),   # for /home/
    path('admin/', custom_admin_view, name='custom_admin'),
]