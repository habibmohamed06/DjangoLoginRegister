from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signin),
    path('signup/', views.newsignup),
    path('accueil/', views.accueil)
]
