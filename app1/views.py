from django.shortcuts import render

# Create your views here.
def bullet(request):
    return render(request,'bullet.html')