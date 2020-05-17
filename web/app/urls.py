from django.urls import path
from .import views

urlpatterns = [
    path('',views.piet,name='piet'),
    path('home',views.piet,name='piet'),
    path('about',views.about,name='about'),
    path('signup',views.signup,name='signup'),
    path('signup_data',views.signup_data,name='signup_data'),
    path('ug',views.ug,name='ug'),
    path('pg',views.pg,name='pg'),
    path('diploma',views.diploma,name='diploma'),
    path('summarized',views.summarized,name='summarized'),
    path('programs',views.programs,name='programs'),
    path('elig',views.elig,name='elig'),
    path('placement',views.placement,name='placement'),
    path('btech',views.btech,name='btech'),
    path('mtech',views.mtech,name='mtech'),
    path('bba', views.bba, name='bba'),
    path('mba', views.mba, name='mba'),
    path('bca', views.bca, name='bca'),
    path('mca', views.mca, name='mca'),
    path('mca2', views.mca2, name='mca2'),
    path('diploma1', views.diploma1, name='diploma1'),
    path('bvoc', views.bvoc, name='bvoc'),
    path('pharmacy', views.pharmacy, name='pharmacy'),

    path('login',views.login,name='login'),
    path('login_data',views.login_data,name='login_data'),

    path('feedbk', views.feedbk, name='feedbk'),
    path('feedbk_data', views.feedbk_data, name='feedbk_data'),

    path('tlogin',views.tlogin,name='tlogin'),
    path('tlogin_data',views.tlogin_data,name='tlogin_data'),

    path('gate',views.gate,name='gate'),
    path('pdf',views.getpdf,name="getpdf")

]
