from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('profile',profile,name='profile'),
    path('features',features,name='features'),
    path('userpolicy',userpolicy,name='userpolicy'),
    path('login/',loginpage,name='loginpage'),
    path('logout',logout,name='logout'),
    path('register',register,name="register"),
    path('feedback',feedback,name="feedback"),
    path('policy0', policy0, name="policy0"),
    path('policy1', policy1, name="policy1"),
    path('policy2', policy2, name="policy2"),
    path('policy3', policy3, name="policy3"),
    path('policy4', policy4, name="policy4"),
    path('policy5', policy5, name="policy5"),
    path('rights', rights, name="rights"),
    path('tc', tc, name="tc"),
    path('theme', theme, name="theme"),
    path('calculator', calculator, name="calculator"),
    path('homeloan',homeloan, name="Hloan"),
    path('eduloan', eduloan, name="Eloan"),
    path('goldloan', goldloan, name="Gloan"),
    path('personalloan', personalloan, name="Ploan"),
    # path('uploadSection',upload,name='upload'),
    path('success', smsg, name="smsg"),
    path('crypto', crypto, name='crypto'),

]