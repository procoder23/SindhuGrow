from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
# from weather_api.key import api_key
import requests
import math
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password,check_password

# Create your views here.
def home(request):
    news_list = News.objects.order_by('id')
    context = {'news_list':news_list}
    return render(request,"app/index.html",context)

def farmer_register_view(request):
     return render(request, "app/registerf.html")

def register_service_provider(request):
    return render(request, "app/registers.html")

def weather_base(request):
    return render(request, "app/base2.html")

def register_hotel_manager(request):
    return render(request, "app/registerh.html")

def farmer_registration_view(request):
    if request.method == "POST":
        # role = request.POST['role']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        area = request.POST['area']
        village = request.POST['village']
        contact = request.POST['contact']
        taluka = request.POST['taluka']
        crop = request.POST['crop']

        user = Usermaster.objects.filter(email=email)

        if user:
            message = "User already Exist"
            return render(request,"app/registerf.html",{'msg':message})
        else:
            newuser = Usermaster.objects.create(email=email, password=make_password(password), role=2)
            newcand = requestFarmer.objects.create(user_id=newuser, firstname=fname, area=area, lastname=lname, village=village,
                                        contact=contact, taluka=taluka, crop=crop)
            return render(request, "app/index.html", {'email': email})

def hotel_registration_view(request):
    if request.method == "POST":
        # role = request.POST['role']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        area = request.POST['area']
        address = request.POST['address']
        contact = request.POST['contact']
        hotel_name = request.POST['hotel_name']
        hotel_contact = request.POST['hotel_contact']

        user = Usermaster.objects.filter(email=email)

        if user:
            message = "User already Exist"
            return render(request,"app/registerh.html",{'msg':message})
        else:
            newuser = Usermaster.objects.create(email=email, password=make_password(password), role=4)
            newcand = requestHotelmanager.objects.create(user_id=newuser, firstname=fname, area=area, address=address,
                                              lastname=lname, contact=contact, hotelname=hotel_name,
                                              hotelcontact=hotel_contact)
            return render(request, "app/index.html", {'email': email})

def service_registration_view(request):
    if request.method == "POST":
        # role = request.POST['role']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        village = request.POST['village']
        area = request.POST['area']
        contact = request.POST['contact']
        taluka = request.POST['taluka']
        equipment = request.POST['equi']

        user = Usermaster.objects.filter(email=email)

        if user:
            message = "User already Exist"
            return render(request,"app/home.html",{'msg':message})
        else:
            newuser = Usermaster.objects.create(email=email, password=make_password(password), role=3)
            newcand = requestServiceprovider.objects.create(user_id=newuser, firstname=fname, area=area, village=village,
                                                 lastname=lname, contact=contact, taluka=taluka, equipment=equipment)
            return render(request, "app/index.html", {'email': email})
    
def loginPage(request):
    return render(request,"app/login.html")

def loginUser(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = Usermaster.objects.get(email=email)
        checkPass = check_password(password,user.password)

        if user:
            if checkPass and user.role == 1:
                admin = User_admin.objects.get(user_id=user)
                request.session['id'] = user.id
                request.session['role'] = user.role
                request.session['email'] = user.email
                print("true")
                return redirect('admindash')
            elif checkPass and user.role == 2:
                farmer = Farmer.objects.get(user_id=user)
                request.session['id'] = user.id
                request.session['role'] = user.role
                request.session['firstname'] = farmer.firstname
                request.session['lastname'] = farmer.lastname
                request.session['village'] = farmer.village
                request.session['area'] = farmer.area
                request.session['contact'] = farmer.contact
                request.session['taluka'] = farmer.taluka
                request.session['crop'] = farmer.crop
                request.session['email'] = user.email 
                print("true")
                return render(request,"app/index.html")
                # return redirect('index')
            elif checkPass and user.role == 3:
                servicep = Serviceprovider.objects.get(user_id=user)
                request.session['id'] = user.id
                request.session['role'] = user.role
                request.session['firstname'] = servicep.firstname
                request.session['lastname'] = servicep.lastname
                request.session['village'] = servicep.village
                request.session['area'] = servicep.area
                request.session['contact'] = servicep.contact
                request.session['taluka'] = servicep.taluka
                request.session['equipment'] = servicep.equipment
                request.session['email'] = user.email
                message="Login Successful"
                return render(request,"app/index.html",{'msg':message})
            elif checkPass and user.role == 4:
                hm = Hotelmanager.objects.get(user_id=user)
                request.session['id'] = user.id
                request.session['role'] = user.role
                request.session['firstname'] = hm.firstname
                request.session['lastname'] = hm.lastname
                request.session['contact'] = hm.contact
                # request.session['ownwephone'] = hm.ownwerphone
                request.session['hotelcontact'] = hm.hotelcontact
                request.session['address'] = hm.address
                request.session['taluka'] = hm.taluka
                request.session['area'] = hm.area
                request.session['hotelname'] = hm.hotelname
                request.session['email'] = user.email
                print("true")
                return redirect('index')
            else:
                message="Password Does Not Match"
                return render(request,"app/login.html",{'msg':message})

        else:
            message="Invalid Login Details"
            return render(request,"app/login.html",{'msg':message})

#@login_required(login_url='login') 
def prod_list(request):
    productlist = Product.objects.order_by('id')
    context = {'productlist':productlist}
    return render(request,"app/list.html",context)

def Logout(request,pk):
    request.session.flush()
    return render(request,"app/index.html")

def service(request):
    servicelist = Service_Details.objects.order_by('id')
    context = {'servicelist':servicelist}
    return render(request,"app/services.html",context)

def hotels(request):
    hotellist = HotelDetails.objects.order_by('id')
    context = {'hotellist':hotellist}
    return render(request,"app/hotelsview.html",context)

def schemes(request):
    schemes_list = Schemes.objects.order_by('id')
    context = {'schemes_list':schemes_list}
    return render(request,"app/schemes.html",context)

def aboutus_page(request):
    return render(request,"app/aboutus.html")

def contactus_page(request):
    return render(request,"app/contactus.html")

def weather(request):
    return render(request,"app/weather/index.html")

def productRequestPage(request):
    return render(request,"app/prodrequest.html")

def requestProduct(request):
    if request.method == "POST":
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        pname = request.POST['productname']
        pprice = request.POST['productprice']
        quality = request.POST['quality']
        freshness = request.POST['freshness']
        date = request.POST['date']
        photu = request.FILES['photu']

        newproduct = Request_Product.objects.create(firstname=fname, lastname=lname, productname=pname,
                                              productprice=pprice, quality=quality,photo=photu,freshness=freshness,
                                              date=date)
        return render(request, "app/profile.html")
    
def requestService(request):
    if request.method == "POST":
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        service = request.POST['equipment']
        rentprice = request.POST['rentprice']
        years = request.POST['years']
        date = request.POST['date']
        photu = request.FILES['photu']

        newproduct = Request_Service.objects.create(firstname=fname, lastname=lname, service=service,
                                              rent=rentprice, years=years,photo= photu,
                                              date=date)
        return render(request, "app/profile.html")
    
def requestHotel(request):
    if request.method == "POST":
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        hotelname = request.POST['hotelname']
        contact = request.POST['contact']
        requirement = request.POST['requirement']
        date = request.POST['date']
        picture = request.FILES['picture']

        newproduct = Request_Hotel.objects.create(firstname=fname, lastname=lname, hotelname=hotelname,
                                              contact=contact, requirement=requirement,image=picture,date=date)
        # user = Usermaster.objects.get(pk=pk)
        # ulist = Request_Hotel.objects.order_by('id')
        # context = {'ulist':ulist}
        return render(request,"app/profile.html")
        

def profilefarmer(request,pk):
    user = Usermaster.objects.get(pk=pk)
    ulist = Request_Product.objects.order_by('id')
    context = {'ulist':ulist}
    return render(request,"app/profile.html",context)

def profilesp(request,pk):
    user = Usermaster.objects.get(pk=pk)
    ulist = Request_Service.objects.order_by('id')
    context = {'ulist':ulist}
    return render(request,"app/profile.html",context)

def profilehm(request,pk):
    user = Usermaster.objects.get(pk=pk)
    ulist = Request_Hotel.objects.order_by('id')
    context = {'ulist':ulist}
    return render(request,"app/profile.html",context)

def updateData(request,pk):
    user = Usermaster.objects.get(pk=pk)

    if user.role == 2:
        udata = Farmer.objects.get(user_id=user)
        udata.firstname = request.POST['firstname']
        udata.lastname = request.POST['lastname']
        udata.contact = request.POST['contact']
        udata.village = request.POST['village']
        udata.area = request.POST['area']
        udata.save()
        user = Usermaster.objects.get(pk=pk)
        # farmer = Farmer.objects.get(user_id=user)
        ulist = Request_Product.objects.order_by('id')
        context = {'ulist':ulist}
        return render(request,"app/profile.html",context)
    
def updateServiceProvider(request,pk):
    user = Usermaster.objects.get(pk=pk)

    if user.role == 3:
        udata = Serviceprovider.objects.get(user_id=user)
        udata.firstname = request.POST['firstname']
        udata.lastname = request.POST['lastname']
        udata.contact = request.POST['contact']
        udata.village = request.POST('village')
        udata.area = request.POST['area']
        udata.save()
        user = Usermaster.objects.get(pk=pk)
        # farmer = Farmer.objects.get(user_id=user)
        ulist = Request_Service.objects.order_by('id')
        context = {'ulist':ulist}
        return render(request,"app/profile.html",context)
    
def updateHotelManager(request,pk):
    user = Usermaster.objects.get(pk=pk)

    if user.role == 4:
        udata = Hotelmanager.objects.get(user_id=user)
        udata.firstname = request.POST['firstname']
        udata.lastname = request.POST['lastname']
        udata.contact = request.POST['contact']
        udata.village = request.POST.get('village')
        udata.area = request.POST['area']
        udata.hotelname = request.POST['hotelname']
        udata.hotelcontact = request.POST['hotelcontact']
        udata.save()
        user = Usermaster.objects.get(pk=pk)
        # farmer = Farmer.objects.get(user_id=user)
        ulist = Request_Hotel.objects.order_by('id')
        context = {'ulist':ulist}
        return render(request,"app/profile.html",context)
    
###############################################################Admin Page#####################################################
@login_required(login_url='login')
def admin_page(request):
    ulist = Usermaster.objects.order_by('id')
    context = {'ulist':ulist}
    return render(request,"app/admin/index.html", context)

def total_farmers(request):
    user_list = Farmer.objects.order_by('id')
    context = {'user_list':user_list}
    return render(request,"app/admin/regisfarmer.html",context)

def total_farmers_register(request):
    user_list = requestFarmer.objects.order_by('id')
    context = {'user_list':user_list}
    
    return render(request,"app/admin/farmerreq.html",context)
def total_sp_register(request):
    user_list = requestServiceprovider.objects.order_by('id')
    context = {'user_list':user_list}
    return render(request,"app/admin/spreq.html",context)

def total_hm_register(request):
    user_list = requestHotelmanager.objects.order_by('id')
    context = {'user_list':user_list}
    return render(request,"app/admin/hmreq.html",context)

def approveFarmer(request,pk):
    farmer = requestFarmer.objects.get(id=pk)
    farmer.approval = 'Approved'
    farmer.save()
    newfarmer = Farmer.objects.create(user_id=farmer.user_id,firstname=farmer.firstname,lastname=farmer.lastname,contact=farmer.contact,village=farmer.village,taluka=farmer.taluka,area=farmer.area,crop=farmer.crop)
    farmer.delete()
    return redirect('admindash')

def approveServicep(request,pk):
    servicep = requestServiceprovider.objects.get(id=pk)
    servicep.approval = 'Approved'
    servicep.save() 
    newsp = Serviceprovider.objects.create(user_id=servicep.user_id,firstname=servicep.firstname,lastname=servicep.lastname,contact=servicep.contact,village=servicep.village,taluka=servicep.taluka,area=servicep.area,equipment=servicep.equipment)
    servicep.delete()
    return redirect('admindash')

def approveHotelm(request,pk):
    hotelm = requestHotelmanager.objects.get(id=pk)
    hotelm.approval = 'Approved'
    hotelm.save()
    newhm = Hotelmanager.objects.create(user_id=hotelm.user_id,firstname=hotelm.firstname,lastname=hotelm.lastname,contact=hotelm.contact,hotelcontact=hotelm.hotelcontact,address=hotelm.address,taluka=hotelm.taluka,area=hotelm.area,hotelname=hotelm.hotelname)
    hotelm.delete()
    return redirect('admindash')

def total_sp(request):
    user_list = Serviceprovider.objects.order_by('id')
    context = {'user_list':user_list}
    return render(request,"app/admin/regisservicep.html",context)

def total_hm(request):
    user_list = Hotelmanager.objects.order_by('id')
    context = {'user_list':user_list}
    return render(request,"app/admin/regishm.html",context)

def loginAdmin(request):
    return render(request,"app/admin/login.html")

def addnews(request):
    user_list = News.objects.order_by('id')
    context = {'user_list':user_list}
    return render(request,"app/admin/addnews.html",context)

def news_add(request):
    if request.method == "POST":
        news = request.POST['news']
        newn = News.objects.create(news=news)
        return render(request,"app/admin/addnews.html")

def schemes_add_page(request):
    schemes_list = Schemes.objects.order_by('id')
    context = {'schemes_list':schemes_list}
    return render(request,"app/admin/addschemes.html",context)

def adding_schemes(request):
    if request.method == "POST":
        title = request.POST['title']
        publishdate = request.POST['publishdate']
        link2 = request.POST['link2']
        print(link2)
        newn = Schemes.objects.create(title=title,publishdate=publishdate,link2=link2)
    return render(request,"app/admin/addschemes.html")

def admindash(request):
    ulist = Usermaster.objects.order_by('id')
    context = {'ulist':ulist}
    return render(request,"app/admin/index.html", context)

def admin_logout(request,pk):
    request.session.flush()
    return render(request,"app/login.html")

def product_request(request):
    plist = Request_Product.objects.order_by('id')
    context = {'plist':plist}
    return render(request,"app/admin/request_prod.html", context)

def appproved_product(request,pk):
    product = Request_Product.objects.get(id=pk)
    product.status = 'Approved'
    product.save()
    newproduct = Product.objects.create(firstname=product.firstname, lastname=product.lastname, productname=product.productname,
                                              productprice=product.productprice, quality=product.quality,photo=product.photo,freshness=product.freshness,
                                              date=product.date)
    plist = Request_Product.objects.order_by('id')
    context = {'plist':plist}
    return render(request,"app/admin/request_prod.html", context)

def total_product(request):
    user_list = Product.objects.order_by('id')
    context = {'user_list':user_list}
    return render(request,"app/admin/productlist.html",context)

def service_request(request):
    slist = Request_Service.objects.order_by('id')
    context = {'slist':slist}
    return render(request,"app/admin/reqservice.html", context)

def appproved_service(request,pk):
    service = Request_Service.objects.get(id=pk)
    service.status = 'Approved'
    service.save()
    newpservice = Service_Details.objects.create(firstname=service.firstname, lastname=service.lastname, service=service.service,
                                              rent=service.rent, years=service.years,photo=service.photo,date=service.date)
    slist = Request_Service.objects.order_by('id')
    context = {'slist':slist}
    return render(request,"app/admin/reqservice.html", context)

def total_services(request):
    service_list = Service_Details.objects.order_by('id')
    context = {'service_list':service_list}
    return render(request,"app/admin/servicelist.html",context)

def request_hotel(request):
    hotellist = Request_Hotel.objects.order_by('id')
    context = {'hotellist':hotellist}
    return render(request,"app/admin/requesthotel.html", context)

def appproved_hotel(request,pk):
    hotel = Request_Hotel.objects.get(id=pk)
    hotel.status = 'Approved'
    hotel.save()
    newhotel = HotelDetails.objects.create(firstname=hotel.firstname, lastname=hotel.lastname, hotelname=hotel.hotelname,
                                              contact=hotel.contact, requirement=hotel.requirement,image=hotel.image,date=hotel.date)
    hotellist = Request_Hotel.objects.order_by('id')
    context = {'hotellist':hotellist}
    return render(request,"app/admin/requesthotel.html", context)

def total_hotels(request):
    hotellist = HotelDetails.objects.order_by('id')
    context = {'hotellist':hotellist}
    return render(request,"app/admin/hotellist.html",context)

def DeleteProduct(request,pk):
    prod = Product.objects.get(id=pk)
    prod.delete()
    return redirect('totalproduct')

def DeleteService(request,pk):
    ser = Service_Details.objects.get(id=pk)
    ser.delete()
    return redirect('totalservices')

def DeleteHotel(request,pk):
    hotel = HotelDetails.objects.get(id=pk)
    hotel.delete()
    return redirect('totalhotels')

def DeleteFarmer(request,pk):
    far = Farmer.objects.get(id=pk)
    far.delete()
    return redirect('tf')

def DeleteServiceProvider(request,pk):
    serp = Serviceprovider.objects.get(id=pk)
    serp.delete()
    return redirect('tsp')

def DeleteHotelManager(request,pk):
    hotelm = Hotelmanager.objects.get(id=pk)
    hotelm.delete()
    return redirect('thm')