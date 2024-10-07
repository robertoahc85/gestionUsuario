from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate ,login 
from django.contrib.auth.decorators import  permission_required , login_required

# Create your views here.

def register(request):
    if request == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.groups.add(request.POST.get('group'))
            login(request, user)
            return redirect ('home')
    else:
        form =UserCreationForm
    return render(request, "register.html", {'form' : form}) 
       

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request ,username=username , password=password)
        if  user is not None:
            login(request,user)
            return redirect('home')
    return render(request,'login.html')    

@permission_required('users.view_ventas',raise_exception=True)
def ventas_view(request):
    return render(request,'ventas.html', {'title': 'Ventas'})

@permission_required('user.view_compras',raise_exception=True)
def compras_view(request):
    return render(request, 'compras.html',{'title':'Compras'})

@permission_required('user.view_inventarios',raise_exception=True)
def inventario_view(request):
    return render(request, 'inventario.html',{'title':'Inventario'})

@login_required
def home(request):
    return render(request,'home.html',{})




