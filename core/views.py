from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from .forms import *
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required


def loginPage(request):
     if request.method=='POST':
          username=request.POST.get('username')
          password=request.POST.get('password')
          user = authenticate(request, username=username,password=password)
          if user is not None:
            login(request,user)
            return redirect('Homepage')
          else:
              return HttpResponse('Invalid credentials')
     else:
         return render(request,'login.html')
     
def signlogin(request):
    return render(request,'signup.html')

def signup(request):
    return render(request,'usersignup.html')

def ethnicpage(request):
    return render(request,'ethnic_wears.html')

def casualpage(request):
    return render(request,'casual_wears.html')

def westernpage(reqeust):
    return render(reqeust,'Western_wears.html')

def aboutpage(request):
    return render(request,'about.html')

def contactpage(request):
    data=contactform.objects.all()
    if request.method=='POST':
        email=request.POST.get('email')
        message=request.POST.get('message')
        details=contactform.objects.create(email=email,message=message)
        details.save()
    return render(request,'contact.html',{'contactlist':data})


def addtocart(request):
    try:
        pid=request.GET.get('pid')
        qty=request.GET.get('qty')
        obj=Product.objects.filter(id=pid).first()
        return render(request,'addtocart.html',{'product':obj,'qty':qty})
    except:
        return HttpResponse("invalid")  

@login_required(login_url='/login/')
def placeorder(request):
     if request.method == 'POST':
        qty=request.POST.get('qty')

        price=request.POST.get('price')
        pdetails=request.POST.get('pdetails')
        
        product=Product.objects.get(id=int(pdetails))
        product.qty-=int(qty)
        product.save()

        order = Order(qty=qty,user=request.user,product=product)
        order.save()
        return redirect('Homepage')
     return HttpResponse("Invalid request")

def details(request):
    try:
        pid=request.GET.get('pid')
        obj=Product.objects.filter(id=pid).first()
        return render(request,'details.html',{'m':obj})
    except:
        return HttpResponse("invalid")
    

class IndexView(View):
    def get(self,request):
        data=blog.objects.all()
        form = ContactForm()
        return render(request,'index.html',{'form':form,'formlist':data, 'login':request.user.is_authenticated})
    
    def post(self,request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'index.html')
        else:
            return HttpResponse('Contact was not saved ')
        
class CategoryView(View):
    templates={
        'western':{'key':0,'template':'Western_wears.html'},
        'ethnic':{'key':1,'template':'ethnic_wears.html'},
        'casual':{'key':2,'template':'casual_wears.html'},
    }

    def get(self,request,name):
        try:
            template=self.templates.get(name).get('template')
            key=self.templates.get(name).get('key')
            products = Product.objects.filter(category=key)
            return render(request,template,{'list':products})
        except:
            return HttpResponse("invalid reqeust")
 
def user_signup1(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('pass1')
        password2=request.POST.get('cpass1')
        if password1==password2:
                new_user=user_signup.objects.create(name=username,email=email,password=password1,con_password=password2)
                new_user.save()
                return redirect(loginPage)
        else:
            print('wrong password')
    return render(request,'usersignup.html')