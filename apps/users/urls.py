from django.urls import path

from . import views


urlpatterns = [
    path('producer_dashboard/',views.panelControl,name='dashboard_producer'),
    path('register/', views.userRegistration, name='register_form')
]