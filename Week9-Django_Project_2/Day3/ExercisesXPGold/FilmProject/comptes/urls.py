from django.urls import path
from comptes import views 

urlpatterns = [
    path('login',views.login_page, name='login'),
    path('logout', views.logout_user,name='logout'),
    path('register',views.signup_page, name='signup'),    
    path('profile/<int:id>',views.profile,name='profile'),


  ]