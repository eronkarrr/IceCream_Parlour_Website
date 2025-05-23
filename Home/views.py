from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from Home.models import Contact

def index(request):
    return render(request,'index.html')
    # return HttpResponse("This is Home Page!")

def about(request):
    return render(request,'about.html')
    # return HttpResponse("This is About Page!")

def services(request):
    return render(request,'services.html')
    # return HttpResponse("This is Services Page!")
   
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Message sent successfully!")
        return redirect('Contact')
    return render(request,'contact.html')
    # return HttpResponse("This is Contact Page!")
   