from django.shortcuts import render,redirect
from .forms import u_signup,issue_book,contact
from .models import user_signup
from django.contrib.auth import logout

# Create your views here.

def index(request):
    if request.method=='POST':
        if request.POST.get('signup')=='signup':
            nusr=u_signup(request.POST)
            if nusr.is_valid():
                nusr.save()
                print("Signup Successfilly....")
                return redirect('home')
            else:
                print(usr.errors)
        elif request.POST.get('login')=='login':
            usremail=request.POST['email']
            usrpassword=request.POST['pasword']
            
            usrid=user_signup.objects.get(email=usremail) # for get_id
            
            usr=user_signup.objects.filter(email=usremail,pasword=usrpassword)
            if usr:
                print("Login Successfully....")
                request.session['user']=usremail
                request.session['usrid']=usrid.id
                return redirect('home')
            else:
                print("Login Fail.....")
    return render(request,'index.html')

def home(request):
    user=request.session.get('user')
    return render(request,'home.html',{'user':user})

def about(requset):
    return render(requset,'about.html')

def contactus(request):
    if request.method=='POST':
        msg=contact(request.POST)
        if msg.is_valid():
            msg.save()
            print("Message Send....")
            return redirect('home')
        else:
            print(msg.errors)  
    return render(request,'contactus.html')

def getbook(request):
    user=request.session.get('user')
    if request.method=='POST':
        ibook=issue_book(request.POST)
        if ibook.is_valid():
            ibook.save()
            print("Book Issue Successfully...")
            return redirect('home')
        else:
            print(ibook.errors)
    return render(request,'getbook.html',{'user':user})


def user_logout(request):
    logout(request)
    return redirect('/')

def update_profile(request):
    user=request.session.get('user')
    uid=request.session.get('usrid')
    id=user_signup.objects.get(id=uid)                                    
    if request.method=='POST':
        sfrm=u_signup(request.POST)
        if sfrm.is_valid():
            sfrm=u_signup(request.POST,instance=id)
            sfrm.save()
            print("Your Profile Data Updated.....")
        else:
            print(sfrm.errors)
            return redirect('home')
    else:
        print("Somthing Wrong....")
    return render(request,'update_profile.html',{'user':user,'userid':user_signup.objects.get(id=uid)})