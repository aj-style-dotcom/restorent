from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import userInfo
# Create your views here.

def signup(req):
    if req.method=="POST":
        fname=req.POST['fname']
        email=req.POST['email']
        uname=req.POST['uname']
        pword=req.POST['pword']
        
        if User.objects.filter(username=uname).exists():
            print("user exist")
            return render(req, 'signup.html', {"message":"user alredy exist, or invalid input"})
        else:
            newUser=User.objects.create_user(username=uname, password=pword, first_name=fname, email=email)
            newUser.save()
            print('user created')
            auth.login(req, newUser)
            return redirect('/')
    else :
        return render(req, 'signup.html')


def signin(req):
    if req.method=="POST":
        uname=req.POST['uname']
        pword=req.POST['pword']

        user=auth.authenticate(username=uname, password=pword)
        if user is not None:
            auth.login(req, user)
            return redirect("/")
        else:
            print('invalid user')
            return render(req, 'signin.html', {"message":"invalid user"})
    else :
        return render(req, 'signin.html')


def logout(req):
    auth.logout(req)
    return redirect('/')


def profile(req):
    if req.method=="POST":
        fname=req.POST['fname']
        email=req.POST['email']
        contact=req.POST['contact']
        address=req.POST['address']

        user=User.objects.get(id=req.user.id)
        user.first_name=fname
        user.email=email

        info=userInfo(user=user, contactNo=contact, address=address)

        user.save()
        info.save()
        return redirect('/')
        

    else :
        user=User.objects.get(id=req.user.id)
        more=userInfo.objects.get(user=user)
        print(more.address)
        return render(req, 'profile.html', {'info':user, 'more':more})