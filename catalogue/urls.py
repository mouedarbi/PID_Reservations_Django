"""reservations.catalogue URL Configuration
"""
from django.urls import path
from django.contrib import admin
from . import views
from .models import Artist

app_name='catalogue'

admin.site.register(Artist)

urlpatterns = [
    path('artist/', views.index, name='artist-index'),
    path('artist/<int:artist_id>', views.show, name='artist-show'),
    path('artist/edit/<int:artist_id>', views.artist.edit, name='artist-edit'),
    path('artist/create',views.artist.create, name='artist-create'),
    path('artist/delete/<int:artist_id>',views.artist.delete, name='artist-delete'),
]
