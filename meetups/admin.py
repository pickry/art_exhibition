from django.contrib import admin

# Register your models here.
from .models import Meetup, Location,Participant
class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title','image')#a tuple
    list_filter = ('location',)
    prepopulated_fields=  {'slug':('title',)}#all that you need to concatanate to make the slug field
class MeetupLocation(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Meetup,MeetupAdmin)
admin.site.register(Location,MeetupLocation)
admin.site.register(Participant)