from django.shortcuts import render

def about(request):
    """About Us 페이지"""
    return render(request, 'pages/about.html')

def home(request):
    """홈 페이지"""
    return render(request, 'home.html')

