from django.urls import path
from  users import views
from django.contrib.auth import  views  as auth_views
from django.conf.urls import handler403

urlpatterns = [
    path('register/',views.register,name='register'),
    path('account/login/',views.login_view,name='login'),
    path('ventas/',views.ventas_view,name='ventas'),
    path('compras/',views.compras_view,name='compras'),
    path('inventarios/',views.inventario_view,name='inventarios'),
    path('logout/',views.logout_view,name='logout'),
    path('',views.home,name='home'),
]

handler403 ='users.views.custom_403_view'