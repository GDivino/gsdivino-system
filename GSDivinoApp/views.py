from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
import os


# Home page
def home(request):
    return render(request, "GSDivinoApp/home.html")


# Aircon 
def view_aircon(request):
    aircon = Aircon.objects.all().order_by("-date")
    return render(request, "GSDivinoApp/view_aircon.html", {"aircon":aircon})

def add_aircon(request):
    if request.method == "POST":
        id = request.POST.get("name")
        date = request.POST.get("date")
        name = FamMember.objects.get(pk=id)

        if Aircon.objects.filter(name=name, date=date).exists() == True:
            messages.error(request, "Aircon day already exists")
            return redirect("add_aircon")
        else:
            Aircon.objects.create(name=name, date=date)
            return redirect("view_aircon") 
    
    fam = FamMember.objects.all()
    return render(request, "GSDivinoApp/add_aircon.html", {"fam":fam})

def update_aircon(request, pk):
    if request.method == "POST":
        name = request.POST.get("name")
        date = request.POST.get("date")

        if Aircon.objects.filter(name=name, date=date).exists() == True:
            messages.error(request, "Aircon day already exists")

            fam = FamMember.objects.all()
            aircon = Aircon.objects.get(pk=pk)
            return render(request, "GSDivinoApp/update_aircon.html", {"aircon":aircon, "fam":fam})
        else:
            Aircon.objects.filter(pk=pk).update(name=name, date=date)
            return redirect("view_aircon")

    fam = FamMember.objects.all()
    aircon = Aircon.objects.get(pk=pk)
    return render(request, "GSDivinoApp/update_aircon.html", {"aircon":aircon, "fam":fam})

def delete_aircon(request, pk):
    Aircon.objects.filter(pk=pk).delete()
    return redirect("view_aircon")


# Dishes
def view_dishes(request):
    dishes = Dish.objects.all().order_by("-date")
    return render(request, "GSDivinoApp/view_dishes.html", {"dishes": dishes})

def add_dish(request):
    if request.method == "POST":
        name_pk = request.POST.get("name")
        date = request.POST.get("date")
        meal = request.POST.get("meal")
        name = FamMember.objects.get(pk=name_pk)

        if Dish.objects.filter(name=name, date=date, meal=meal).exists() == True:
            messages.error(request, "Dish data already exists")
            return render(request, "GSDivinoApp/add_dish.html")
        else:
            Dish.objects.create(name=name, date=date, meal=meal)
            return redirect("view_dishes")
    
    fam = FamMember.objects.all()
    return render(request, "GSDivinoApp/add_dish.html", {"fam":fam})

def update_dish(request, pk):
    if request.method == "POST":
        name_pk = request.POST.get("name")
        date = request.POST.get("date")
        meal = request.POST.get("meal")
        name = get_object_or_404(FamMember, pk=name_pk)

        if Dish.objects.exclude(name=name, date=date, meal=meal).filter(name=name, date=date, meal=meal).exists() == True:
            messages.error(request, "Dish data already exists")

            dish = Dish.objects.get(pk=pk)
            fam = FamMember.objects.all()
            return render(request, "GSDivinoApp/update_dish.html", {"fam":fam, "dish":dish})
        else:
            Dish.objects.filter(pk=pk).update(name=name, date=date, meal=meal)
            return redirect("view_dishes")
    
    dish = Dish.objects.get(pk=pk)
    fam = FamMember.objects.all()
    return render(request, "GSDivinoApp/update_dish.html", {"fam":fam, "dish":dish})

def delete_dish(request, pk):
    Dish.objects.filter(pk=pk).delete()
    return redirect("view_dishes")


# Laundry
def view_laundry(request):
    laundry = Laundry.objects.all()
    return render(request, "GSDivinoApp/view_laundry.html", {"laundry": laundry})

def add_laundry(request):
    if request.method == "POST":
        name_pk = request.POST.get("name")
        date = request.POST.get("date")
        name = FamMember.objects.get(pk=name_pk)

        if Laundry.objects.filter(name=name, date=date).exists() == True:
            messages.error(request, "Laundry data already exists")
            return render(request, "GSDivinoApp/add_laundry.html")
        else:
            Laundry.objects.create(name=name, date=date)
            return redirect("view_laundry")
    
    fam = FamMember.objects.all()
    return render(request, "GSDivinoApp/add_laundry.html", {"fam":fam})

def delete_laundry(request, pk):
    Laundry.objects.filter(pk=pk).delete()
    return redirect("view_laundry")

def update_laundry(request, pk):
    if request.method == "POST":
        name_pk = request.POST.get("name")
        date = request.POST.get("date")
        name = get_object_or_404(FamMember, pk=name_pk)

        if Laundry.objects.exclude(name=name, date=date).filter(name=name, date=date).exists() == True:
            messages.error(request, "Laundry data already exists")

            laundry = Laundry.objects.get(pk=pk)
            fam = FamMember.objects.all()
            return render(request, "GSDivinoApp/update_laundry.html", {"fam":fam, "laundry":laundry})
        else:
            Laundry.objects.filter(pk=pk).update(name=name, date=date)
            return redirect("view_dishes")
    
    laundry = Laundry.objects.get(pk=pk)
    fam = FamMember.objects.all()
    return render(request, "GSDivinoApp/update_laundry.html", {"fam":fam, "laundry":laundry})



#Bills
def view_bills(request):
    bills = Bill.objects.all()
    return render(request, "GSDivinoApp/view_bills.html", {"bills": bills})

def add_bill(request):
    if request.method == "POST":
        name = request.POST.get("name")
        status = request.POST.get("status")
        price = request.POST.get("price")
        due_date = request.POST.get("date")

        if Bill.objects.filter(name=name, status=status, price=price, due_date=due_date).exists() == True:
            messages.error(request, "Bill entry already exists")
            return render(request, "GSDivinoApp/add_bill.html")
        else:
            Bill.objects.create(name=name, status=status, price=price, due_date=due_date)
            return redirect("view_bills")
    return render(request, "GSDivinoApp/add_bill.html")

def delete_bill(request, pk):
    Bill.objects.filter(pk=pk)
    return redirect("view_bill")

def update_bill(request, pk):
    if request.method == "POST":
        name = request.POST.get("name")
        status = request.POST.get("status")
        price = request.POST.get("price")
        due_date = request.POST.get("date")

        if Bill.objects.exclude(name=name, status=status, price=price, due_date=due_date).filter(name=name, status=status, price=price, due_date=due_date).exists() == True:
            messages.error(request, "Bill entry already exists")

            bill = get_object_or_404(Bill, pk=pk)
            return render(request, "GSDivinoApp/update_bill.html", {"bills":bill})

        else:
            Bill.objects.filter(pk=pk).update(name=name, status=status, price=price, due_date=due_date)
            return redirect("view_bills")

    bill = get_object_or_404(Bill, pk=pk)
    return render(request, "GSDivinoApp/update_bill.html", {"bill":bill})