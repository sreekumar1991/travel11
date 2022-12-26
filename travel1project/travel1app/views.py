from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from.models import Place


# Create your views here.
def demo(request):
    obj=Place.objects.all()
    return render(request,"index.html",{'result':obj})