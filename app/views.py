from django.shortcuts import redirect, render
from .models import productModel, orderModel
from user.models import userInfo
# Create your views here.


def home(req):
    all_dish=productModel.objects.all()
    return render(req, 'home.html', {"dishesh":all_dish})


def single(req, id):
    item=productModel.objects.get(id=id)
    info=None
    try:
        info=userInfo.objects.get(user=req.user.id)
    except:
        pass
    return render(req, 'single.html', {"dish":item, "info":info})


def brackfast(req):
    list=productModel.objects.filter(category="Brackfast")
    return render(req, 'category.html', {
        "list":list,
        "page":"Brackfast"
        })



def lunch(req):
    list=productModel.objects.filter(category="Lunch")
    return render(req, 'category.html', {
        "list":list,
        "page":"Lunch"
        })



def dinner(req):
    list=productModel.objects.filter(category="Dinner")
    return render(req, 'category.html', {
        "list":list,
        "page":"Dinner"
        })


def snacks(req):
    list=productModel.objects.filter(category="Snacks")
    return render(req, 'category.html', {
        "list":list,
        "page":"Snacks"
        })

    

def searchresult(req):
    dishName=req.POST['dishName']
    try:
        item=productModel.objects.get(name=dishName)
        info=userInfo.objects.get(user=req.user.id)
        return render(req, 'single.html', {"dish":item, "info":info})
    except:
        return render(req, 'notFound.html')


def orderItem(req, itemID):
    quantity=req.POST['quantity']
    item=productModel.objects.get(id=itemID)
    newOrder=orderModel(user=req.user, itemID=itemID, quantity=quantity)
    newOrder.save()
    context={
        "name":item.name,
        "image":item.image.url,
        "prize":item.prize,
        "quantity":quantity,
        "total":item.prize * int(quantity)
    }
    return render(req, "orderPage.html", context)