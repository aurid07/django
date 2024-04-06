from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('upload', views.upload, name='upload'),
    path('follow', views.follow, name='follow'),
    path('search', views.search, name='search'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('like-post', views.like_post, name='like-post'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('add-note/', views.add_note, name='add_note'),
    path('edit-note/<int:note_id>/', views.edit_note, name='edit_note'),
    path('delete-note/<int:note_id>/', views.delete_note, name='delete_note'),
    path('step_count/', views.step_count, name='step_count'),
    path('edit_step_count/<int:step_count_id>/', views.edit_step_count, name='edit_step_count'),
    path('delete_step_count/<int:step_count_id>/', views.delete_step_count, name='delete_step_count'),
    path('step_count_leaderboard/', views.step_count_leaderboard, name='step_count_leaderboard'),
]