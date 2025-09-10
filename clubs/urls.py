from django.urls import path
from . import views


urlpatterns = [
    path('clubs',views.clubs, name='clubs'),
    path('<int:pk>',views.club_details,name="club_details"),
    path('api/clubs/', views.ClubListView.as_view(), name='club-list'),
]