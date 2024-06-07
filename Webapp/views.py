from django.shortcuts import render,redirect
from Backend.models import Productdb,categorydb
from Webapp.models import contactinfodb,registrationdb

# Create your views here.

def home_page(request):
    cat = categorydb.objects.all()
    return render(request,"home.html",{'cat':cat})

def about_page(request):
    return render(request,"about.html")

def contact_page(request):
    return render(request,"contact.html")

def product_page(request):
    pro = Productdb.objects.all()
    return render(request,"products.html",{'pro':pro})

def save_contact(request):
    if request.method=="POST":
        cna = request.POST.get('name')
        csub = request.POST.get('subject')
        cmail = request.POST.get('email')
        cmes = request.POST.get('message')
        cph = request.POST.get('phone')
        obj=contactinfodb(cname=cna,cmessage=cmes,cphone=cph,cemail=cmail,csubject=csub)
        obj.save()
        return redirect(contact_page)

def products_filtered(request,cat_name):
    data = Productdb.objects.filter(pcategory=cat_name)
    return render(request,"product_filtered.html",{'data':data})


def single_product(request,pro_id):
    data=Productdb.objects.get(id=pro_id)
    return render(request,"single_product.html",{'data':data})

def registration_page(req):
    return render(req,"registration_page.html")

def save_registration(req):
    if req.method=="POST":
        na=req.POST.get('name')
        em=req.POST.get('email')
        pas=req.POST.get('password')
        img=req.FILES['image']
        obj=registrationdb(Name=na,Email=em,Password=pas,Image=img)
        obj.save()
        return redirect(registration_page)

