from django.shortcuts import render, redirect
from .models import Quote, Contact
# Create your views here.
def index(request):
    return render(request, "main/index.html")
def aboutus(request):
    return render(request, "main/aboutus.html")
def services(request):
    return render(request, "main/services.html")
def quote(request):
    return render(request, "main/quote.html")
def processquote(request):
    form = request.POST 
    quote =  Quote.objects.create(description = form["description"], first_name = form["first_name"], last_name = form["last_name"], company= form["company"], phone = form["phone"], email = form["email"], location = form["location"], custcategory = form["custcategory"], truckcategory = form["truckcategory"], prevailing = form["prevailing"], hours = form["hours"])
    request.session["newquote"] = quote.id
    return redirect("/quotedone")
def quotedone(request):
    newquote = Quote.objects.get(id = request.session["newquote"])
    context = {
        "quote": newquote
    }
    return render(request, "main/quotedone.html", context)
def green(request):
    return render(request,"main/green.html")
def contact(request):
    return render(request,"main/contact.html")
def processcontact(request):
    form = request.POST 
    message =  Contact.objects.create(first_name = form["first_name"], last_name = form["last_name"],company= form["company"], phone = form["phone"], email = form["email"], location = form["location"], interestedIn = form["interestedIn"], message= form["message"])
    request.session["newmessage"] = message.id
    return redirect("/contactdone")
def contactdone(request):
    newmessage = Contact.objects.get(id = request.session["newmessage"])
    context = {
        "message": newmessage
    }
    return render(request, "main/contactdone.html", context)
def pay(request):
    return render(request, "main/payonline.html")
def processpayment(request):
    return redirect('/paymentdone')
def paymentdone(request):
    return render(request, "main/paymentdone.html")
def careers(request):
    return render(request, "main/careers.html")