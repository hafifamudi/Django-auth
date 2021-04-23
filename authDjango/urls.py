from django.urls import path

from . import views

app_name = 'authDjango'
urlpatterns = [
  path('', views.IndexView.as_view(), name='index'),
  path('register/', views.RegisterView.as_view(), name='register'),
  path('register/user-register/', views.RegisterUserView.as_view(), name='user_register'),
  path('login/', views.LoginView.as_view(), name='login'),
  path('login/user-login', views.LoginUserView.as_view(), name='user_login'),
  path('logout/', views.LogoutView.as_view(), name='logout')
]