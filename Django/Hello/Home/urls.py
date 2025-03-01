from django.contrib import admin
from django.urls import path
from Home import views

admin.site.site_header = "ICE CREAM Admin"
admin.site.site_title = "ICE CREAM Admin Portal"
admin.site.index_title = "Welcome to ICE CREAM Portal"

urlpatterns = [
   path("" , views.index , name = 'home'),
   path("about" , views.about , name = 'about'),
   path("services" , views.services , name = 'services'),
   path("contact" , views.contact , name = 'contact'),
   path('flavour', views.flavour, name='flavour'),
   path("cart", views.cart, name="cart"),
   path("checkout", views.checkout, name="checkout"),
   
   
   path("login", views.login_view, name='login'),
    path('register', views.register_view, name='register'),
    path('logout', views.logout_view, name='logout'),
    path('dashboard', views.dashboard_view, name='dashboard')
]
