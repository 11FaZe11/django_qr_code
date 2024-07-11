from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('success/', success, name='success'),
    path('logout/', logoutUser, name='logout'),
]