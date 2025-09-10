from django.urls import path

from . import views

urlpatterns = [
    
    path('register/<int:event_id>/',views.register_event,name='register_event')
]