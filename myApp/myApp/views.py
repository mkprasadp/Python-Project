from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

def Home(request):
    return render(request,'Home.html',{'Homepage':"Welcome Home"})

@csrf_exempt
def Loginpage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pass')
        
        if email == '' and password == '':
            return render(request,'Loginpage.html',{'error':'Email and Password cannot be empty'})
        elif email != 'example@gmail.com':
            return render(request,'Loginpage.html',{'error':'Invalid Email address'})
        elif password != 'Admin@1618':
            return render(request,'Loginpage.html',{'error':'Invalid Password'})
        else:
            request.session['email'] = email
            Home = reverse('Home')
            submit_form = reverse('submit_form')
            return render(request,'logout.html',{'email':email,'Home':Home,'submit_form':submit_form})
    else:
        return render(request,'Loginpage.html')

def Registration(request):
    return render(request, 'Registration.html')

@csrf_exempt
def submit_form(request):
    if request.method == 'POST':
        data = request.POST.get('name')
        return HttpResponse(f'<h1 style="color:red">{data}</h1>')
    else:
        return render(request,'form.html')