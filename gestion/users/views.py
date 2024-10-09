from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate ,login , logout
from django.contrib.auth.decorators import  permission_required , login_required
from .form import CustomUserCreationForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect ('home')
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {'form' : form}) 
       

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request ,username=username , password=password)
        if  user is not None:
            login(request,user)
            return redirect('home')
    return render(request,'login.html',{'error':'Credenciales invalidas'})    

@permission_required('users.view_ventas',raise_exception=True)
def ventas_view(request):
    return render(request,'ventas.html', {'title': 'Ventas'})

@permission_required('users.view_compras',raise_exception=True)
def compras_view(request):
    return render(request, 'compras.html',{'title':'Compras'})

@permission_required('users.view_inventarios',raise_exception=True)
def inventario_view(request):
    return render(request, 'inventarios.html',{'title':'Inventario'})

@login_required
def logout_view(request):
    logout(request)
    return render(request,'logout.html')

@login_required
def home(request):
    user = request.user
    context = {
        'can_view_ventas': user.has_perm('users.view_ventas'),
        'can_view_compras': user.has_perm('users.view_compras'),
        'can_view_inventarios': user.has_perm('users.view_inventarios'),
        
    }
    return render(request,'home.html', context)

def custom_403_view(request, exception):
    return render(request, '403.html', status=403)
    


