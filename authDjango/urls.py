from django.urls import path

from . import views

app_name = 'authDjango'
urlpatterns = [
  path('', views.IndexView.as_view(), name='index'),
  path('register/', views.RegisterView.as_view(), name='register'),
  path('register/user-register/', views.RegisterUserView.as_view(), name='user_register')
]