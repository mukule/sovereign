from django.urls import path
from . import views



app_name = 'main'
urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path('hero/', views.hero, name='hero'),
    path('seniors/', views.seniors, name='seniors'),
    path('create-senior/', views.create_senior, name='create_senior'),
    path('senior/edit/<int:senior_id>/', views.edit_senior, name='edit_senior'),
    path('senior/delete/<int:senior_id>/', views.delete_senior, name='delete_senior'),
    path('companies/', views.companies, name='companies'),
    path('create-company/', views.create_company, name='create_company'),
    path('company/edit/<int:pk>/', views.edit_company_profile, name='edit_company_profile'),
    path('company/delete/<int:pk>/', views.delete_company_profile, name='delete_company_profile'),
    path('company/detail/<int:pk>/', views.company_profile_detail, name='company_profile_detail'),
    path('events/', views.events, name='events'),
    path('create-event/', views.create_event, name='create_event'),
    path('events/edit/<int:event_id>/', views.edit_event, name='edit_event'),
    path('events/delete/<int:event_id>/', views.delete_event, name='delete_event'),
]