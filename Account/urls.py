from django.contrib.auth import views as auth_views
from django.urls import path, re_path

from . import views
from django.contrib.auth import views as auth_views
app_name = 'account'

urlpatterns = [
    re_path(r'^customerView/$', views.customerView, name='customerView'),
    path("technicianView/", views.technicianView, name='technicianView'),
    path("", views.home, name="home"),
    path("login/", auth_views.LoginView.as_view(), name="user_login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("availableTechs/", views.availableTechs, name="availableTechs"),
    path("registration/", views.registration_view.as_view(), name="user_registration"),
    path("gallery/", views.gallery, name='gallery'),
    path("services/", views.services, name='services'),
    path("aboutUs/", views.aboutUs, name='aboutUs'),
    path("profile/", views.profile, name='profile'),
    path("changePassword/", views.changePassword, name='changePassword'),
    path("securitySettings/", views.securitySettings, name='security'),
    path("editAddress/", views.edit_address, name='edit_address'),
    path("deleteAccount/", views.deleteAccount, name='deleteAccount'),
    path("changeEmail/", views.changeEmail, name='changeEmail'),
    path("techSchedule/", views.techSchedule, name="techSchedule")
]
