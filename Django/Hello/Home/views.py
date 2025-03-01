from django.shortcuts import render , HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages 
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login , logout , authenticate 
 

# Create your views here.
def index (request):
    return render(request , 'index.html')
    # return HttpResponse("This is Home Page")
    

def about (request):
    return render(request , 'about.html')
    # return HttpResponse("This is About Page")


def services (request):
    return render(request , 'services.html')
    # return HttpResponse("This is Services Page")
    
    
def flavour (request):
    return render(request , 'flavour.html')

def cart (request):
    return render(request ,'cart.html')

def checkout (request):
    return render(request ,'checkout.html')
    

def contact (request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name , email=email,desc=desc , date = datetime.today())
        contact.save()
        
        if name and email and desc:  # Ensure all fields are filled
            contact = Contact(name=name, email=email, desc=desc, date=datetime.today())
            contact.save()
            
            messages.success(request, "Your message has been sent successfully! ✅")
            return redirect('/contact')  # Redirect to prevent form resubmission
        else:
            messages.error(request, "All fields are required. Please try again. ❌")
        
        
        
    return render(request , 'contact.html')
    # return HttpResponse("This is contact Page")
    
    
    # auth
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('dashboard')
    else:
        initial_data = {'username':'', 'password1':'','password2':""}
        form = UserCreationForm(initial=initial_data)
    return render(request, 'register.html',{'form':form})


# def login_view(request):
#     return HttpResponse("Login Page Loaded Successfully!")
# def login_view(request):
#     return render(request, 'login.html', {})



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('dashboard')
    else:
        initial_data = {'username':'', 'password':''}
        form = AuthenticationForm(initial=initial_data)
    return render(request, 'login.html',{'form':form}) 


def dashboard_view(request):
    return render(request, 'dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('home')