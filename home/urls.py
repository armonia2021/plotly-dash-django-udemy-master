from django.urls import path
from . import views
from home.dash_apps.finished_apps import simpleexample
from home.dash_apps.finished_apps import app
from home.dash_apps.finished_apps import app_user, tabel, table_amministrazione


urlpatterns = [
    path('', views.home, name='home'),
    path('welcome.html', views.home, name='home'),
    #path('login.html',views.login, name='home'),
    path('dashboard.html',views.dashboard, name='home'),
    path('index.html', views.index, name='home'),
    path('form.html', views.form, name='home'),
    #path('country',views.country_form, name='home'),
    path("register", views.register_request, name="home"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    #path('login.html', views.home, name='login')
    path("tables.html",views.form, name="home"),

]