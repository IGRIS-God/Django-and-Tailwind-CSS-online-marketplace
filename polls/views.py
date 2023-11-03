from django.contrib.auth import logout
from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignupForm
from django.contrib.auth.decorators import login_required
from conversation.models import Conversation

def index(request):
    items = Item.objects.filter(is_sold=False)[0:5]
    categories= Category.objects.all()
    
    if request.user.is_authenticated:
        conversations = Conversation.objects.filter(members__in=[request.user.id])
        unread_messages_count = conversations.filter(has_unread_messages=True).count()
    else:
        unread_messages_count = 0
        
    return render(request, 'polls/index.html',{
        'categories': categories,
        'items': items,
        'unread_messages_count': unread_messages_count
    })    

def contact(request):
    return render(request, 'polls/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('/login/')
    else:
        form = SignupForm()
    
    return render(request, 'polls/signup.html',{
        'form': form
    })

def LogoutView(request):
    logout(request)
    return redirect('index')
