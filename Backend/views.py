from django.shortcuts import render,redirect
from Backend.models import categorydb,Productdb
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from Webapp.models import contactinfodb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages
# Create your views here.
def index_page(request):
    return render(request,"index.html")

def category(request):
    return render(request,"category.html")

def save_category(request):
    if request.method=="POST":
        cna=request.POST.get('cname')
        cdes=request.POST.get('cdescription')
        cimg=request.FILES['cimage']
        obj=categorydb(cname=cna,cdescription=cdes,cimage=cimg)
        obj.save()
        messages.success(request,"Category Added Successfully....!")
        return redirect(category)

def display_category(request):
    data = categorydb.objects.all()
    return render(request,"display_category.html",{'data': data})

def edit_category(request,c_id):
    cat = categorydb.objects.filter(id=c_id)
    return render(request,"edit_category.html",{'cat':cat})

def update_category(request,c_id):
    cn=request.POST.get('cname')
    cd=request.POST.get('cdescription')
    try:
        img=request.FILES['cimage']
        fs=FileSystemStorage()
        file=fs.save(img.name,img)
    except MultiValueDictKeyError:
        file=categorydb.objects.get(id=c_id).product_images
    categorydb.objects.filter(id=c_id).update(cname=cn,cdescription=cd,cimage=file)
    return redirect(display_category)

def delete_category(request,c_id):
    data=categorydb.objects.filter(id=c_id)
    data.delete()
    messages.success(request, "Category Successfully Deleted!")
    return redirect(display_category)

def login_page(request):
    return render(request,"login_page.html")

def admin_login(request):
    if request.method == "POST":
        un = request.POST.get('username')
        ps = request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un,password=ps)

            if x is not None:
                login(request,x)
                request.session['username'] = un
                request.session['password'] = ps
                messages.success(request,"Welcome")
                return redirect(index_page)
            else:
                messages.warning(request,"Invalid Username Or Password")
                return redirect(login_page)
        else:
            messages.warning(request, "User Not Found")
            return redirect(login_page)


def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(login_page)

def product_page(req):
    cat = categorydb.objects.all()
    return render(req,"add_product.html",{'cat':cat})

def save_product(request):
    if request.method=="POST":
        pcat=request.POST.get('pcat')
        pna=request.POST.get('pname')
        pdes=request.POST.get('pdescription')
        pprice=request.POST.get('pprice')
        pimg=request.FILES['pimage']
        obj = Productdb(pcategory=pcat,pname=pna, pdescription=pdes, pimage=pimg,pprice=pprice)
        obj.save()
        messages.success(request, "Product Added Successfully....!")
        return redirect(product_page)


def display_product(request):
    data = Productdb.objects.all()
    return render(request,"display_product.html",{'data': data})

def edit_product(request,pro_id):
    pro = Productdb.objects.filter(id=pro_id)
    cat = categorydb.objects.all()
    return render(request,"edit_product.html",{'pro':pro},{'cat':cat})


def update_product(request,pro_id):
    pn=request.POST.get('pname')
    pr=request.POST.get('pprice')
    pdes=request.POST.get('pdescription')
    try:
        img=request.FILES['pimage']
        fs=FileSystemStorage()
        file=fs.save(img.name,img)
    except MultiValueDictKeyError:
        file=Productdb.objects.get(id=pro_id).pimage
    Productdb.objects.filter(id=pro_id).update(pname=pn,pprice=pr,pdescription=pdes,pimage=file)
    return redirect(display_product)






def delete_product(request,pro_id):
    data = Productdb.objects.filter(id=pro_id)
    data.delete()
    messages.success(request, "Product Successfully Deleted!")
    return redirect(display_product)

def contact_info(request):
    data=contactinfodb.objects.all()
    return render(request,"contact_data.html",{'data':data})

def delete_cinfo(request,i_id):
    data=contactinfodb.objects.filter(id=i_id)
    data.delete()
    return redirect(contact_info)












