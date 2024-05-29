from django.urls import path
from . import views

urlpatterns = [
    path('member/', views.memberlist, name='member'),
    path('member/details/<int:id>', views.details, name='details'),
    path('',views.main,name='main'),
    path('register/', views.newUser, name='register'),

]