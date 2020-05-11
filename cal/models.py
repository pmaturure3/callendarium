from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django.utils import timezone
# from filer.fields.image import FilerImageField


class Event(models.Model):
    """
    Calendar Events
    """
    CSS_CLASS_CHOICES = (
        ('', _('Normal')),
        ('event-warning', _('Warning')),
        ('event-info', _('Info')),
        ('event-success', _('Success')),
        ('event-inverse', _('Inverse')),
        ('event-special', _('Special')),
        ('event-important', _('Important')),
    )
    Event_Type = models.ForeignKey(
        'EventType', on_delete=models.CASCADE, related_name='type', null=True, blank=True)
    News = 'News'
    Events = 'Events'
    Opportunities = 'Opportunities'

    EVENT_CHOICES = (
        ('News', 'News'),
        ('Events', 'Events'),
        ('Opportunities', 'Opportunities'),
    )
    event_choice = models.CharField(
        max_length=20, choices=EVENT_CHOICES, null=True, blank=True)

    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = models.TextField(max_length=20000, null=True, blank=True)
    #event_image = FilerImageField(null=True, blank=True, related_name ="events_images", on_delete=models.SET_NULL)
    speaker = models.CharField(max_length=2000, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    url = models.TextField(verbose_name=_('URL'), null=True, blank=True)
    css_class = models.CharField(blank=True, max_length=20, verbose_name=_('CSS Class'),
                                 choices=CSS_CLASS_CHOICES, null=True)
    start_time = models.DateTimeField(verbose_name=_('Start Date'))
    end_time = models.DateTimeField(verbose_name=_('End Date'), null=True,
                                    blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    #updated_at = models.DateTimeField(default=timezone.now())

    @property
    def start_timestamp(self):
        """
        Return start date as timestamp
        """
        return self.start_time

    @property
    def end_timestamp(self):
        """
        Return end date as timestamp
        """
        return self.end_time

    def __str__(self):
        return self.title

    @property
    def image(self):
        return self.event_image.file


class EventType(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Event type"

    def __str__(self):
        return self.name
