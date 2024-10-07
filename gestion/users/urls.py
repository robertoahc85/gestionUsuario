from django.urls import path
from  users import views
from django.contrib.auth import  views  as auth_views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login_view,name='login'),
    path('ventas/',views.ventas_view,name='ventas'),
    path('compras/',views.compras_view,name='compras'),
    path('inventario/',views.inventario_view,name='inventarios'),
    path('logout/',auth_views.LogoutView.as_view(template_name="logout.html"),name='logout'),
    path('',views.home,name='home'),
]