from django.shortcuts import render

# Create your views here.
def relHome(request):
    
    return render(request,'relation/index.html')
