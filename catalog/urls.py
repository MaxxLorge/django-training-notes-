from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('reg/', views.reg, name='reg'),
    path('auth/', views.auth, name='auth'),
    path('logout/', views.user_logout, name='logout'),
    path('user_data/', views.UserList.as_view(), name='user_list'),
    path('user_data/<int:pk>', views.UserDetailed.as_view(), name='user_list'),
    path('notes_data/', views.NotesList.as_view(), name='notes_list'),
]