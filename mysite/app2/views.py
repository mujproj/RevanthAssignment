from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.


    

def afterFileUpload(request):
    if(request.method == "POST"):
        
        print(request.FILES['file'])
        user = FileUpload(jsonFile=request.FILES["file"])
        user.save()
        return render(request, 'inde.html')
    
    else:
        return render(request, 'fileupload.html')
        
        
def displayFiles(request):
    files = FileUpload.objects.all()
    return render(request, 'filedisplay.html',{'files': files})