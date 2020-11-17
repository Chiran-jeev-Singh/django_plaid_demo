# from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.index, name='index'),
    path('users/login/', views.login, name='login'),
    path('users/logout/', views.logout, name='logout'),
    path('users/signup/', views.signup, name='signup'),
    path('users/account/profile/<int:user_id>/', views.account_profile, name='account_profile'),
    path('users/validate/', views.validate, name='validate'),
    path('users/invalidate/', views.invalidate, name='invalidate'),
 	path('users/register/', views.register, name='register'),
 	path('users/getTransactions/', views.getTransactions, name='getTransactions'),
 	path('users/getAccounts/', views.getAccounts, name='getAccounts'),
    
]
