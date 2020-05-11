from django.urls import path
from cal import views

app_name = "cal"

urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('schedule/', views.CalendarView.as_view(), name="calendar"),
    path('events/', views.calendar_events, name="calendar_events"),
]
