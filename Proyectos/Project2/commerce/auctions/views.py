from email import message
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect , get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import User,auction,watchlist,category
from asyncio.windows_events import NULL
from .forms import AuctionForm


def index(request):
    if request.method == 'GET':
        return render(request, "auctions/index.html",{
        'auctions':auction.objects.all(),
        'categories': category.objects.all()
        })
   

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")



def createlisting (request):
    if not request.user.is_authenticated:
        return render(request, 'auctions/error.html',{
            'message': 'You Have To Log In'
        })
    if request.method == 'GET':
        return render(request, "auctions/createlisting.html",{
        'auctions':auction.objects.all(),
        'categories': category.objects.all()
        })
    else:
        
        t=request.POST['title']
        d=request.POST['description']
        p=request.POST['price']
        p=int(p)
        i=request.FILES['image']
        if len(t)==0 or p==0:
            return render(request,'auctions/createlisting.html')

        else:
            auc=auction.objects.create(Article=t,Description=d,Price=p, Image=i)
            auc.save()
        return render(request, "auctions/index.html",{
        'auctions':auction.objects.all(),
        'categories': category.objects.all()
        
        })




def Watchlist(request, id=NULL):
    if not request.user.is_authenticated:
        return render(request, 'auctions/error.html',{
            'message': 'You Have To Log In'
        })

    else: 
        if id==NULL:
              return render(request, "auctions/watchlist.html",{
                'lists': watchlist.objects.all(),
                'categories': category.objects.all()
                
                })
        
        else:
            if request.method == 'POST':
                prod=auction.objects.get(id=id)
                t=prod.Article
                d=prod.Description
                p=prod.Price
                p=int(p)
                i=prod.Image
                if len(t)==0 or p==0:
                    return render(request,'auctions/createlisting.html')

                else:
                    auc=watchlist.objects.create(Article=t,Description=d,Price=p, Image=i)
                    auc.save()
                return render(request, "auctions/watchlist.html",{
                'lists':watchlist.objects.all(),
                'categories': category.objects.all()
                
                })

    

def Error(request):
    return render (request, 'auctions/error.html',{
       'message': 'You have to log in'
    })

def Product(request,article):
    watchlist=True
    prod=auction.objects.get(Article=article)
    

    return render(request,'auctions/product.html',{
        'pro':prod,
        'watchlist':watchlist
    })

def categories(request):
    if request.method=='POST':
        cat=request.POST['category']
        cat1=category.objects.get(CategorieName=cat)
        auct=auction.objects.filter(Category=cat1)
        if cat == 'All':
            return render(request, "auctions/index.html",{
            'auctions':auction.objects.all(),
            'categories': category.objects.all()
            })
    return render(request, "auctions/index.html",{
        'auctions': auct,
        'categories': category.objects.all()
        })

def delete(request,Article):
    if request.method == 'POST':
        prod=watchlist.objects.get(Article=Article)
        prod.delete()
        return redirect ('watchlist')

def create(request):
        
    form = AuctionForm()

    return render(request, 'auctions/form2.html',{
        'form':form,
        })
   