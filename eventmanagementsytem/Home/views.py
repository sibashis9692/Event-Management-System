from django.shortcuts import render, HttpResponse, redirect
from Home.models import sibashislocation, sibashisevents, sibashislogin

def home(request):
    return render(request, "index.html")
def event(request):
    data=None
    if "user" in request.session.keys():
        data=sibashisevents.objects.filter(email = request.session["user"]).all()
    context={
        "items": data
    }
    return render(request, "Events.html", context)

def location(request):
    data=None
    data=sibashislocation.objects.all()
    context={
        "items": data
    }
    return render(request, "Location.html", context)

def creatEvent(request):
    if(request.method == "POST"):
        title=request.POST.get("title")
        description=request.POST.get("description")
        date=request.POST.get("date")
        cost=request.POST.get("cost")
        location=request.POST.get("location")
        data=sibashisevents(email=request.session["user"], tittle=title, description=description, date=date, cost=cost, location=location)
        data.save()
        return redirect("/event/")
    return render(request, "creatEvent.html")

def creatLocation(request):
    if(request.method == "POST"):
        name=request.POST.get("name")
        address=request.POST.get("address")
        manager=request.POST.get("manager")
        email=request.POST.get("email")
        data=sibashislocation(name=name, address=address, manager=manager, email=email)
        data.save()
        return redirect("/location/")
    return render(request, "creatLocation.html")

def login(request):
    request.session["notexists"]=False
    if(request.method == "POST"):
        email=request.POST.get("email")
        password=request.POST.get("password")
        entery=sibashislogin.objects.filter(email = email).first()
        if(entery != None and entery.password != password):
            return HttpResponse("<h1>Password Incorect</h1><p> <a href=/login/> Try Again </a></p>")
        elif(entery == None):
            context={
                "email": email
            }
            request.session["notexists"]=True
            return render(request, "login.html", context)
        else:
            request.session["user"]=email
            request.session["logedin"]=True
            return redirect("/")
    return render(request, "login.html")

def register(request):
    request.session["exists"]=False
    if(request.method == "POST"):
        email=request.POST.get("email")
        password=request.POST.get("password")
        repassword=request.POST.get("repassword")
        data=sibashislogin.objects.filter(email = email).first()
        if(data != None):
            request.session["exists"]=True
            context={
                "email":data.email
            }
            return render(request, "register.html", context)
        elif(data == None and password != repassword):
            return HttpResponse("<h1>Password and RePassword is Not same</h1><p> <a href=/register/> Try Again </a></p>")
        entery=sibashislogin(email = email, password = password)
        entery.save()
        request.session["notexists"] = False
        return render(request, "login.html")
    return render(request, "register.html")

def logout(request):
    request.session["logedin"]=False
    return redirect("/")

def editing(request, c, number):
    if(c == "e"):
        data=sibashisevents.objects.filter(sno=number).first()
        context={
            "items":data
        }
        return render(request, "show.html", context)
    else:
        data=sibashislocation.objects.filter(sno=number).first()
        context={
            "items":data
        }
        return render(request, "show.html", context)
def delete(request, c, number):
    if(c == "e"):
        data=sibashisevents.objects.filter(sno=number).first()
        data.delete()
        return redirect("/event/")
    else:
        data=sibashislocation.objects.filter(sno=number).first()
        data.delete()
        return redirect("/location/")
        
def editEvent(request, number):
    if(request.method == "POST"):
        title=request.POST.get("title")
        description=request.POST.get("description")
        date=request.POST.get("date")
        cost=request.POST.get("cost")
        location=request.POST.get("location")
        data=sibashisevents.objects.filter(sno=number).first()
        data.tittle=title
        data.description=description
        data.date=date
        data.cost=cost
        data.location=location
        data.save()
        return redirect("/event/")
    else:
        data=sibashisevents.objects.filter(sno = number).first()
        context={
            "items":data
        }
        return render(request, "showEvents.html", context)
    
def editLocation(request, number):
    if(request.method == "POST"):
        name=request.POST.get("name")
        address=request.POST.get("address")
        manager=request.POST.get("manager")
        email=request.POST.get("email")
        data=sibashislocation.objects.filter(sno = number).first()
        data.name=name
        data.address=address
        data.manager=manager
        data.email=email
        data.save()
        return redirect("/location/")
    else:
        data=sibashislocation.objects.filter(sno = number).first()
        context={
            "items":data
        }
        return render(request, "showLocation.html", context)