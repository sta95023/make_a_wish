from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt
import datetime
def index(request):
    request.session.clear()
    return render( request,"wish/reg_and_log.html")
def register(request): # Post
    pw_hash = bcrypt.hashpw(request.POST['user_password'].encode(), bcrypt.gensalt())
    errors = Users.objects.basic_validator(request.POST)
    if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/")
    u = Users.objects.create(first_name = request.POST["user_firstname"], last_name = request.POST["user_lastname"], email = request.POST["user_email"], password = pw_hash)
    request.session['my_val'] = u.id
    return redirect('/wishes')
def login(request):

    listOfmatchingUsers = Users.objects.filter(email = request.POST['user_email'])
    if bcrypt.checkpw(request.POST['user_password'].encode(), listOfmatchingUsers[0].password.encode()):
        request.session['my_val'] = listOfmatchingUsers[0].id
        return redirect('/wishes')
    else:
        return redirect ("/")
def wishingApp(request):
    context = {
        'user_firstname': Users.objects.get(id=request.session['my_val']).first_name,
        'all_wishes': Wishes.objects.filter(granted_by=None),
        'granted_wishes': Wishes.objects.exclude(granted_by=None)
    }
    return render(request, "wish/wishing_app.html", context)
def likeButton(request):
    return redirect("/wishes")
def newWish(request):
    context = {
        'user_firstname': Users.objects.get(id=request.session['my_val']).first_name,
    }
    return render (request, "wish/new_wish.html")
def createWish(request):
    errors = Wishes.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/wishes/new")
    if request.method =="POST":
        w = Wishes.objects.create(thing = request.POST["wish_thing"], description = request.POST["wish_description"], posted_by=Users.objects.get(id=request.session['my_val']))
        request.session['my_num'] = w.id
    return redirect("/wishes")
def editWish(request, my_num): # Get
    if request.method == "GET":

        context = {
            'user_firstname': Users.objects.get(id=request.session['my_val']).first_name,
            'wish':Wishes.objects.get(id=my_num),
            }
        return render(request, "wish/edit_wish.html", context)
def editWisUpdate(request): # Post
    if request.method == "POST":
        wishes_to_update = Wishes.objects.get(id=request.POST["bob"])
        wishes_to_update.thing = request.POST["wish_thing"]
        wishes_to_update.description = request.POST["wish_description"]
        wishes_to_update.save()
    return redirect("/wishes")
def grantedWishs(request, my_num):
    if request.method == "GET":
        context = {
            'user_firstname': Users.objects.get(id=request.session['my_val']).first_name,
            'wish':Wishes.objects.get(id=my_num),
            }
    return render(request, "wish/view_wish.html", context)
def grantWish(request, my_num):
    this_wish = Wishes.objects.get(id=my_num)
    this_wish.granted_by = Users.objects.get(id=request.session['my_val'])
    this_wish.save()
    return redirect("/wishes")
def delete(request, my_num):
    Wishes.objects.get(id=my_num).delete()
    return redirect("/wishes")
def logOut(request):
    request.session.clear()
    return redirect("/")