from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('<int:pk>/', views.DetailView.as_view(), name='details'),
    path('album/add/', views.CreateAlbum.as_view(), name='add_album'),
    path('register/', views.UserFormView.as_view(), name='register'),
    # path('<int:album_id>/favourite/', views.favourite, name='favourite')
]
