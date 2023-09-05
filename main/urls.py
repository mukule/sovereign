from django.urls import path
from . import views



app_name = 'main'
urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path('hero/', views.hero, name='hero'),
    path('seniors/', views.seniors, name='seniors'),
    path('create-senior/', views.create_senior, name='create_senior'),
    path('companies/', views.companies, name='companies'),
    path('create-company/', views.create_company, name='create_company'),
    path('events/', views.events, name='events'),
    path('create-event/', views.create_event, name='create_event'),
]