from django.contrib import admin
from .models import *

# Personnalisation de l'affichage des modèles dans l'admin

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname')
    search_fields = ('firstname', 'lastname')


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('type',)
    search_fields = ('type',)


@admin.register(ArtistType)
class ArtistTypeAdmin(admin.ModelAdmin):
    list_display = ('artist', 'type')
    list_filter = ('type',)
    autocomplete_fields = ('artist', 'type')


@admin.register(ArtistTypeShow)
class ArtistTypeShowAdmin(admin.ModelAdmin):
    list_display = ('artist_type', 'show')
    list_filter = ('show',)


@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_in', 'bookable', 'location')
    list_filter = ('bookable', 'created_in', 'location')
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('designation', 'slug', 'locality', 'phone')
    list_filter = ('locality',)
    search_fields = ('designation', 'slug', 'address')
    prepopulated_fields = {'slug': ('designation',)}


@admin.register(Locality)
class LocalityAdmin(admin.ModelAdmin):
    list_display = ('locality', 'postal_code')
    search_fields = ('locality', 'postal_code')


@admin.register(Representation)
class RepresentationAdmin(admin.ModelAdmin):
    list_display = ('show', 'schedule', 'location')
    list_filter = ('schedule', 'location', 'show')
    date_hierarchy = 'schedule'


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('type', 'price', 'start_date', 'end_date')
    list_filter = ('start_date', 'end_date')
    date_hierarchy = 'start_date'


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'booking_date', 'status')
    list_filter = ('status', 'booking_date', 'user')
    date_hierarchy = 'booking_date'


@admin.register(RepresentationReservation)
class RepresentationReservationAdmin(admin.ModelAdmin):
    list_display = ('reservation', 'representation', 'price', 'quantity')
    list_filter = ('price', 'representation__schedule')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'show', 'stars', 'validated', 'created_at')
    list_filter = ('validated', 'stars', 'created_at', 'show')
    date_hierarchy = 'created_at'


@admin.register(UserMeta)
class UserMetaAdmin(admin.ModelAdmin):
    list_display = ('user', 'langue')
    search_fields = ('user__username', 'user__first_name', 'user__last_name')