from django.contrib import admin
from cal import models


class EventAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "event_choice", "description",
                    "speaker", "location", "url", "css_class", "start_time", "end_time", "created"]
    list_filter = ["event_choice", "start_time"]


class EventTypeAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description", "created"]


admin.site.register(models.Event, EventAdmin)
admin.site.register(models.EventType, EventTypeAdmin)
