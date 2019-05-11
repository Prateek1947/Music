from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('(?P<album_id>[0-9]+)/)',views.details)
]
