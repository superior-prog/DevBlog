from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    # path('', home, name='home'),

    # user login and logout url
    path('accounts/login', login_page, name='login'),
    path('accounts/logout', logout_user, name='logout'),

    # applicant registration url
    path('accounts/signup', user_register, name='user-register'),
]
