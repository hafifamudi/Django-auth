from django.urls import path

from . import views

app_name = 'userShop'
urlpatterns = [
  path('', views.UserView.as_view(), name='index'),
]