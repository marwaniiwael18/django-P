from django.contrib import admin
from .models import Person, Event, User, Participation

# Register your models here.

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('cin', 'email')
    search_fields = ('cin', 'email')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'state', 'evt_date', 'nbe_participant', 'organizer')
    list_filter = ('category', 'state', 'evt_date', 'creation_date')
    search_fields = ('title', 'description')
    date_hierarchy = 'evt_date'
    
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('cin', 'email', 'django_user')
    search_fields = ('cin', 'email')

@admin.register(Participation)
class ParticipationAdmin(admin.ModelAdmin):
    list_display = ('person', 'event', 'participation_date')
    list_filter = ('participation_date', 'event__category')
    search_fields = ('person__cin', 'event__title')
