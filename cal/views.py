from django.core import serializers
from datetime import datetime, date, timedelta
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import generic
from django.utils.safestring import mark_safe
from .models import *
from .utils import Calendar


def home_page(request):
    return HttpResponse("Welcome to Django")


# The api endpoints
def calendar_events(request):
    events = []
    for event in Event.objects.all():
        events.append({
            'title': event.title,
            'event_choice': event.event_choice,
            'description': event.description,
            'location': event.location,
            'url': event.url,
            'css_class': event.css_class,
            'start': event.start_time,
            'end': event.end_time,
        })

    return JsonResponse(events, safe=False)


class CalendarView(generic.TemplateView):
    template_name = 'cal/calendar.html'


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month
