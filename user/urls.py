from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    # path('', home, name='home'),

    # user login and logout url
    path('account/login', login_page, name='login'),
    path('account/logout', logout_user, name='logout'),

    # applicant registration url
    path('account/user-registration', user_register, name='user-register'),
]
