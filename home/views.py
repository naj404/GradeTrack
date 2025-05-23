from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def home_view(request):
    return render(request, 'home/home.html')

def custom_admin_view(request):
    return render(request, 'home/admin.html')

