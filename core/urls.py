from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('room/<str:room_name>/', views.room, name='room'),
    path('board/', views.board, name='board')
]

urlpatterns += staticfiles_urlpatterns()
